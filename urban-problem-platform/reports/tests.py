from django.test import TestCase
from .models import Report

class ReportModelTest(TestCase):

    def setUp(self):
        Report.objects.create(
            problem_type="Pothole",
            description="Large pothole on main street",
            location="Conakry",
            status="Open"
        )

    def test_report_creation(self):
        report = Report.objects.get(problem_type="Pothole")
        self.assertEqual(report.description, "Large pothole on main street")
        self.assertEqual(report.location, "Conakry")
        self.assertEqual(report.status, "Open")