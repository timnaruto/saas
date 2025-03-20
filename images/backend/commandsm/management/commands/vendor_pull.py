import helpers
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

VENDOR_STATICFILES = {
    "saas-theme.min.css": "https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Downloading vendor static files')
        complete_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            # Print statement aligned properly (optional, for debugging)
            print(f"Downloading: {name} from {url} to {out_path}")

            if dl_success:
                self.stdout.write(self.style.SUCCESS(f"Successfully downloaded {name}"))
                complete_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {name} from {url}"))

        # Optional: Summary of completed downloads
        self.stdout.write(f"Completed downloads: {len(complete_urls)} out of {len(VENDOR_STATICFILES)}")