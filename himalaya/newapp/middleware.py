from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import UploadedImage, IPAddress


class ImageUploadLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware is called!")
        client_ip = self.get_client_ip(request)
        if self.exceeds_upload_limit(client_ip):
            return HttpResponseForbidden("Upload limit exceeded for this IP address.")
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        print("Getting client IP...")
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(f"Client IP: {ip}")
        return ip

    def exceeds_upload_limit(self, client_ip):
        print(f"Checking upload limit for IP: {client_ip}")
        max_uploads_per_day = 10
        current_time = timezone.now()
        time_window = current_time - timezone.timedelta(days=1)

        try:
            ip_address_obj = IPAddress.objects.get(ip=client_ip)
        except IPAddress.DoesNotExist:
            ip_address_obj = IPAddress.objects.create(ip=client_ip)

        UploadedImage.objects.filter(
            ip_address=ip_address_obj,
            timestamp__lt=time_window
        ).delete()

        upload_count = UploadedImage.objects.filter(
            ip_address=ip_address_obj,
            timestamp__gte=time_window
        ).count()

        print(f"Upload count for IP {client_ip}: {upload_count}")

        return upload_count >= max_uploads_per_day
