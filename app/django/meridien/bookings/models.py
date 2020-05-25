from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Booking(models.Model):
    ACCEPTED = ('ACC', 'Accepted')
    REJECTED = ('REJ', 'Rejected')
    PENDING = ('PEN', 'Pending')

    BOOKING_STATUSES = [
        ACCEPTED,
        REJECTED,
        PENDING
    ]
    
    name = models.CharField(max_length=256, blank=False, default='N/A')
    email = models.EmailField(blank=False, default='N/A')
    organization = models.CharField(max_length=1000, blank=False, default='N/A')
    reason = models.TextField(blank=False, default='-')
    time_booked = models.DateTimeField(auto_now_add=True)
    loan_start_time = models.DateField(blank=False, default=date.fromtimestamp(0))
    loan_end_time = models.DateField(blank=False, default=date.fromtimestamp(0))
    deposit_left = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, validators=[MinValueValidator(0.00), MaxValueValidator(200.00)])
    status = models.CharField(max_length=32, blank=False, default=PENDING)
