# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from baham.models import VehicleModel, Vehicle, Contract, UserProfile
from baham.enum_types import VehicleType, VehicleStatus
from baham.constants import COLOURS
from django.utils.timezone import now
from datetime import datetime, date, timedelta
from schedule.periods import Period
from schedule.models.events import Event
from django.db.models import Q


class VehicleContractTest(TestCase):
    def setUp(self):
        start = datetime(2023, 5, 27, 00, 00, 00, 0)
        end = datetime(2023, 6, 5, 23, 59, 59, 0)
        event = Event(start, end)
        self.superuser = User.objects.create_superuser(username='admin', email='admin@dareecha.com', password='admin')
        self.owner = User.objects.create_user(username='user', email='a@gmail.com', password='123')
        self.companion = UserProfile.objects.create(user=self.owner, birthdate=date(2000,2,3), user_id=1)
        self.model = VehicleModel.objects.create(vendor='KIET', model='Unicorn-1', type=VehicleType.VAN, capacity=3)
        self.vehicle1 = Vehicle.objects.create(registration_number='ABC-877', colour=COLOURS[7], 
                                               model=self.model, owner=self.owner, status=VehicleStatus.AVAILABLE)
        self.contract = Contract.objects.create(effective_start_date=start, expiry_date=end, is_active=True, fuel_share=25,
                                       maintenance_share=50, schedule=Period(event, start=start, end=end), 
                                       vehicle_id=self.vehicle1.vehicle_id, companion_id=self.companion.id)
        return super().setUp()
    #Test Case #1
    def test_one_vehicle_per_owner(self):
        vehicle2 = Vehicle.objects.create(registration_number='ABC-878', colour=COLOURS[9], model=self.model, 
                                           owner=self.owner, status=VehicleStatus.AVAILABLE)
        self.assertEqual(Vehicle.objects.filter(owner=self.owner).count(), 1, 'No Owner can own 2 Vehicles')
    #Test Case #2
    def test_passengers_less_than_capacity(self):
        with self.assertRaises(Exception):
            self.contract = Contract.objects.create(effective_start_date=self.start, expiry_date=self.end, is_active=True, fuel_share=25,
                                       maintenance_share=50, schedule=Period(self.event, start=self.start, end=self.end), 
                                       vehicle_id=self.vehicle1.vehicle_id, companion_id=self.companion.id)
            raise
        
    #Test Case #3
    def test_total_share_exceed_limit_100(self):
        #For Fuel + Maintenance Share
        ctr = Contract.objects.get(contract_id = self.contract.contract_id)
        fs = getattr(ctr, 'fuel_share')
        ms = getattr(ctr, 'maintenance_share')
        self.assertLess(fs+ms, 100)
    
    #Test Case #4
    def test_companions_multiple_contracts(self):
        
        with self.assertRaises(Exception) as context:
            Contract.objects.create(effective_start_date=self.start+timedelta(days=2), expiry_date=self.end+timedelta(days=2), is_active=True, fuel_share=25,
                                       maintenance_share=50, schedule=Period(self.event, start=self.start+timedelta(days=2), end=self.end+timedelta(days=2)), 
                                       vehicle_id=self.vehicle1.vehicle_id, companion_id=self.companion.id)
            
            raise

        cond1 = Q(companion_id=self.contract.companion.id)
        cond2 = Q(is_active=True)
        self.assertEqual(Contract.objects.filter(cond1 & cond2).count(), 1)
    

    def tearDown(self):
        UserProfile.objects.all().delete()
        Vehicle.objects.all().delete()
        Contract.objects.all().delete()
        User.objects.all().delete()
