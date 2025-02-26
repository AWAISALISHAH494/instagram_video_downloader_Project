# # from django.shortcuts import render

# # # Create your views here.
# # from django.http import JsonResponse, FileResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from django.conf import settings
# # import instaloader
# # import os
# # import shutil
# # import re
# # import random
# # from urllib.parse import urlparse
# # import logging
# # from fake_useragent import UserAgent
# # import json

# # logger = logging.getLogger(__name__)

# # # Initialize Instaloader with random user-agent
# # ua = UserAgent()
# # L = instaloader.Instaloader(
# #     download_video_thumbnails=False,
# #     save_metadata=False,
# #     user_agent=ua.random
# # )

# # # Directory for temporary downloads
# # DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # # Instagram URL pattern
# # INSTAGRAM_URL_PATTERN = r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)"

# # def clean_download_dir():
# #     """Clean up the download directory before each new request."""
# #     if os.path.exists(DOWNLOAD_DIR):
# #         shutil.rmtree(DOWNLOAD_DIR)
# #     os.makedirs(DOWNLOAD_DIR)

# # def validate_url(url):
# #     """Validate if the provided URL is a valid Instagram post/reel/IGTV URL."""
# #     return re.match(INSTAGRAM_URL_PATTERN, url) is not None

# # def extract_shortcode(url):
# #     """Extract the Instagram shortcode from the URL."""
# #     parsed_url = urlparse(url)
# #     path = parsed_url.path.strip('/')
# #     parts = path.split('/')
# #     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
# #         return parts[1]
# #     return None

# # def index(request):
# #     return render(request, 'index.html')

# # @csrf_exempt  # Disable CSRF for simplicity (enable in production with proper setup)
# # def download_content(request):
# #     """Handle the download request."""
# #     if request.method != 'POST':
# #         return JsonResponse({'error': 'Method not allowed'}, status=405)

# #     try:
# #         # Parse JSON body
# #         data = json.loads(request.body)
# #         url = data.get('url', '').strip()

# #         if not url or not validate_url(url):
# #             return JsonResponse({'error': 'Invalid Instagram URL'}, status=400)

# #         # Extract shortcode
# #         shortcode = extract_shortcode(url)
# #         if not shortcode:
# #             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

# #         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode})")

# #         # Clean previous downloads
# #         clean_download_dir()

# #         # Update user-agent for this request
# #         L.context._session.headers['User-Agent'] = ua.random

# #         # Download the post
# #         post = instaloader.Post.from_shortcode(L.context, shortcode)
# #         L.download_post(post, target=DOWNLOAD_DIR)

# #         # Find the downloaded file(s)
# #         downloaded_files = []
# #         for file in os.listdir(DOWNLOAD_DIR):
# #             file_path = os.path.join(DOWNLOAD_DIR, file)
# #             if os.path.isfile(file_path) and file.endswith(('.mp4', '.jpg', '.jpeg', '.png')):
# #                 downloaded_files.append(file_path)

# #         if not downloaded_files:
# #             return JsonResponse({'error': 'No downloadable content found'}, status=404)

# #         # Send the first file (extend for carousels if needed)
# #         file_to_send = downloaded_files[0]
# #         logger.info(f"Sending file: {file_to_send}")

# #         return FileResponse(
# #             open(file_to_send, 'rb'),
# #             as_attachment=True,
# #             filename=os.path.basename(file_to_send)
# #         )

# #     except instaloader.exceptions.ConnectionException as e:
# #         logger.error(f"Connection error: {str(e)}")
# #         return JsonResponse({'error': 'Connection issue with Instagram. Please try again later.'}, status=503)
# #     except instaloader.exceptions.InvalidArgumentException:
# #         logger.error("Invalid Instagram shortcode")
# #         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
# #     except json.JSONDecodeError:
# #         return JsonResponse({'error': 'Invalid request body'}, status=400)
# #     except Exception as e:
# #         logger.error(f"Unexpected error: {str(e)}")
# #         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# # from django.http import JsonResponse, FileResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from django.conf import settings
# # from django.shortcuts import render
# # import instaloader
# # import os
# # import shutil
# # import re
# # from urllib.parse import urlparse
# # import logging
# # from fake_useragent import UserAgent
# # import json

# # logger = logging.getLogger(__name__)

# # ua = UserAgent()
# # L = instaloader.Instaloader(
# #     download_video_thumbnails=False,
# #     save_metadata=False,
# #     user_agent=ua.random
# # )

# # DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # INSTAGRAM_URL_PATTERN = r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)"

# # def clean_download_dir():
# #     if os.path.exists(DOWNLOAD_DIR):
# #         shutil.rmtree(DOWNLOAD_DIR)
# #     os.makedirs(DOWNLOAD_DIR)

# # def validate_url(url):
# #     return re.match(INSTAGRAM_URL_PATTERN, url) is not None

# # def extract_shortcode(url):
# #     parsed_url = urlparse(url)
# #     path = parsed_url.path.strip('/')
# #     parts = path.split('/')
# #     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
# #         return parts[1]
# #     return None

# # def index(request):
# #     return render(request, 'index.html')

# # @csrf_exempt
# # def download_content(request):
# #     if request.method != 'POST':
# #         return JsonResponse({'error': 'Method not allowed'}, status=405)

# #     try:
# #         data = json.loads(request.body)
# #         url = data.get('url', '').strip()

# #         if not url or not validate_url(url):
# #             return JsonResponse({'error': 'Invalid Instagram URL'}, status=400)

# #         shortcode = extract_shortcode(url)
# #         if not shortcode:
# #             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

# #         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode})")
# #         clean_download_dir()
# #         L.context._session.headers['User-Agent'] = ua.random

# #         post = instaloader.Post.from_shortcode(L.context, shortcode)
# #         L.download_post(post, target=DOWNLOAD_DIR)

# #         downloaded_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
# #         if not downloaded_files:
# #             return JsonResponse({'error': 'No downloadable content found'}, status=404)

# #         file_to_send = os.path.join(DOWNLOAD_DIR, downloaded_files[0])
# #         logger.info(f"Sending file: {file_to_send}")

# #         return FileResponse(
# #             open(file_to_send, 'rb'),
# #             as_attachment=True,
# #             filename=os.path.basename(file_to_send),
# #             content_type='application/octet-stream'
# #         )

# #     except instaloader.exceptions.ConnectionException as e:
# #         logger.error(f"Connection error: {str(e)}")
# #         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
# #     except instaloader.exceptions.InvalidArgumentException:
# #         logger.error("Invalid Instagram shortcode")
# #         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
# #     except json.JSONDecodeError:
# #         return JsonResponse({'error': 'Invalid request body'}, status=400)
# #     except Exception as e:
# #         logger.error(f"Unexpected error: {str(e)}")
# #         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent
# import json

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# INSTAGRAM_URL_PATTERN = r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)"

# def clean_download_dir():
#     if os.path.exists(DOWNLOAD_DIR):
#         shutil.rmtree(DOWNLOAD_DIR)
#     os.makedirs(DOWNLOAD_DIR)

# def validate_url(url):
#     return re.match(INSTAGRAM_URL_PATTERN, url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# def index(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         data = json.loads(request.body)
#         url = data.get('url', '').strip()

#         if not url or not validate_url(url):
#             return JsonResponse({'error': 'Invalid Instagram URL'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

#         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode})")
#         clean_download_dir()
#         L.context._session.headers['User-Agent'] = ua.random

#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=DOWNLOAD_DIR)

#         downloaded_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#         if not downloaded_files:
#             logger.warning(f"No files found in {DOWNLOAD_DIR} for {shortcode}")
#             return JsonResponse({'success': 'Download Successful'}, status=404)

#         file_to_send = os.path.join(DOWNLOAD_DIR, downloaded_files[0])
#         logger.info(f"Sending file: {file_to_send}")

#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_to_send)}"'
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         logger.error(f"Connection error: {str(e)}")
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         logger.error("Invalid Instagram shortcode")
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except json.JSONDecodeError:
#         logger.error("Invalid JSON in request body")
#         return JsonResponse({'error': 'Invalid request body'}, status=400)
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent
# import json

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# INSTAGRAM_URL_PATTERN = r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)"

# def clean_download_dir():
#     if os.path.exists(DOWNLOAD_DIR):
#         shutil.rmtree(DOWNLOAD_DIR)
#     os.makedirs(DOWNLOAD_DIR)

# def validate_url(url):
#     return re.match(INSTAGRAM_URL_PATTERN, url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# def index(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         data = json.loads(request.body)
#         url = data.get('url', '').strip()

#         if not url or not validate_url(url):
#             return JsonResponse({'error': 'Invalid Instagram URL'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

#         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode})")
#         clean_download_dir()
#         L.context._session.headers['User-Agent'] = ua.random

#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=DOWNLOAD_DIR)

#         downloaded_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#         if not downloaded_files:
#             logger.warning(f"No files found in {DOWNLOAD_DIR} for {shortcode}")
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         file_to_send = os.path.join(DOWNLOAD_DIR, downloaded_files[0])
#         logger.info(f"Sending file: {file_to_send}")

#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_to_send)}"'
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         logger.error(f"Connection error: {str(e)}")
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         logger.error("Invalid Instagram shortcode")
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except json.JSONDecodeError:
#         logger.error("Invalid JSON in request body")
#         return JsonResponse({'error': 'Invalid request body'}, status=400)
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# INSTAGRAM_URL_PATTERN = r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)"

# def clean_download_dir():
#     if os.path.exists(DOWNLOAD_DIR):
#         shutil.rmtree(DOWNLOAD_DIR)
#     os.makedirs(DOWNLOAD_DIR)

# def validate_url(url):
#     return re.match(INSTAGRAM_URL_PATTERN, url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# def index(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         # Change: Use request.POST instead of request.body
#         url = request.POST.get('url', '').strip()

#         if not url or not validate_url(url):
#             return JsonResponse({'error': 'Invalid Instagram URL'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

#         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode})")
#         clean_download_dir()
#         L.context._session.headers['User-Agent'] = ua.random

#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=DOWNLOAD_DIR)

#         downloaded_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#         if not downloaded_files:
#             logger.warning(f"No files found in {DOWNLOAD_DIR} for {shortcode}")
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         file_to_send = os.path.join(DOWNLOAD_DIR, downloaded_files[0])
#         logger.info(f"Sending file: {file_to_send}")

#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_to_send)}"'
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         logger.error(f"Connection error: {str(e)}")
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         logger.error("Invalid Instagram shortcode")
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# import uuid
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# # Define DOWNLOAD_DIR globally, but we'll override it per request
# DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# def get_unique_download_dir():
#     unique_dir = os.path.join(settings.MEDIA_ROOT, 'downloads', str(uuid.uuid4()))
#     os.makedirs(unique_dir, exist_ok=True)
#     return unique_dir

# def clean_download_dir():
#     if os.path.exists(DOWNLOAD_DIR):
#         shutil.rmtree(DOWNLOAD_DIR)
#     os.makedirs(DOWNLOAD_DIR)

# def validate_url(url):
#     return re.match(r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)", url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# def index(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         logger.info("Method not allowed: Not a POST request")
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         logger.info(f"Received POST data: {request.POST}")
#         url = request.POST.get('url', '').strip()
#         if not url:
#             logger.warning("No URL provided")
#             return JsonResponse({'error': 'No URL provided'}, status=400)
#         if not validate_url(url):
#             logger.warning(f"Invalid URL: {url}")
#             return JsonResponse({'error': f'URL "{url}" does not match Instagram format'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             logger.warning(f"Could not extract shortcode from URL: {url}")
#             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

#         download_dir = get_unique_download_dir()
#         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode}) in {download_dir}")
#         L.context._session.headers['User-Agent'] = ua.random

#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=download_dir)

#         downloaded_files = [f for f in os.listdir(download_dir) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#         logger.info(f"Files found in {download_dir}: {downloaded_files}")
#         if not downloaded_files:
#             logger.warning(f"No files found in {download_dir} for {shortcode}")
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         file_to_send = os.path.join(download_dir, downloaded_files[0])
#         logger.info(f"Sending file: {file_to_send}")

#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_to_send)}"'
#         logger.info(f"Returning file response for: {file_to_send}")
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         logger.error(f"Connection error: {str(e)}")
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         logger.error("Invalid Instagram shortcode")
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except Exception as e:
#         logger.exception(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# import uuid
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent
# import time  # Add this import

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# def get_unique_download_dir():
#     unique_dir = os.path.join(settings.MEDIA_ROOT, 'downloads', str(uuid.uuid4()))
#     os.makedirs(unique_dir, exist_ok=True)
#     return unique_dir

# DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# def clean_download_dir():
#     if os.path.exists(DOWNLOAD_DIR):
#         shutil.rmtree(DOWNLOAD_DIR)
#     os.makedirs(DOWNLOAD_DIR)

# def validate_url(url):
#     return re.match(r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)", url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# def index(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         logger.info("Method not allowed: Not a POST request")
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         logger.info(f"Received POST data: {request.POST}")
#         url = request.POST.get('url', '').strip()
#         if not url:
#             logger.warning("No URL provided")
#             return JsonResponse({'error': 'No URL provided'}, status=400)
#         if not validate_url(url):
#             logger.warning(f"Invalid URL: {url}")
#             return JsonResponse({'error': f'URL "{url}" does not match Instagram format'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             logger.warning(f"Could not extract shortcode from URL: {url}")
#             return JsonResponse({'error': 'Could not extract shortcode from URL'}, status=400)

#         download_dir = get_unique_download_dir()
#         logger.info(f"Processing download for URL: {url} (Shortcode: {shortcode}) in {download_dir}")
#         L.context._session.headers['User-Agent'] = ua.random

#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=download_dir)

#         # Wait briefly and retry to ensure file is written
#         retries = 5
#         for _ in range(retries):
#             downloaded_files = [f for f in os.listdir(download_dir) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#             if downloaded_files:
#                 break
#             logger.info(f"No files yet in {download_dir}, retrying...")
#             time.sleep(0.5)  # Wait 0.5 seconds before retrying

#         if not downloaded_files:
#             logger.warning(f"No files found in {download_dir} for {shortcode} after retries")
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         file_to_send = os.path.join(download_dir, downloaded_files[0])
#         logger.info(f"Sending file: {file_to_send}")

#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_to_send)}"'
#         logger.info(f"Returning file response for: {file_to_send}")
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         logger.error(f"Connection error: {str(e)}")
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         logger.error("Invalid Instagram shortcode")
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except Exception as e:
#         logger.exception(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
# from django.http import JsonResponse, FileResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render
# import instaloader
# import os
# import shutil
# import re
# import uuid
# from urllib.parse import urlparse
# import logging
# from fake_useragent import UserAgent
# import time

# logger = logging.getLogger(__name__)

# ua = UserAgent()
# L = instaloader.Instaloader(
#     download_video_thumbnails=False,
#     save_metadata=False,
#     user_agent=ua.random
# )

# # Define the system's Downloads folder
# MAIN_DOWNLOAD_FOLDER = os.path.expanduser("~/Downloads")

# def get_unique_download_dir():
#     """Create a unique directory for the current download session."""
#     unique_dir = os.path.join(settings.MEDIA_ROOT, 'downloads', str(uuid.uuid4()))
#     os.makedirs(unique_dir, exist_ok=True)
#     return unique_dir

# def index(request):
#     return render(request, 'index.html')

# def validate_url(url):
#     """Validate Instagram URL format."""
#     return re.match(r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)", url) is not None

# def extract_shortcode(url):
#     """Extract shortcode from Instagram URL."""
#     parsed_url = urlparse(url)
#     path = parsed_url.path.strip('/')
#     parts = path.split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

#     try:
#         url = request.POST.get('url', '').strip()
#         if not url:
#             return JsonResponse({'error': 'No URL provided'}, status=400)
#         if not validate_url(url):
#             return JsonResponse({'error': f'Invalid URL: {url}'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             return JsonResponse({'error': 'Could not extract shortcode'}, status=400)

#         download_dir = get_unique_download_dir()
#         logger.info(f"Downloading {url} (Shortcode: {shortcode}) into {download_dir}")

#         L.context._session.headers['User-Agent'] = ua.random
#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=download_dir)

#         # Wait for the file to be written
#         retries = 5
#         for _ in range(retries):
#             downloaded_files = [f for f in os.listdir(download_dir) if f.endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#             if downloaded_files:
#                 break
#             time.sleep(0.5)

#         if not downloaded_files:
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         # Get the first file (assumed to be the correct file)
#         file_to_send = os.path.join(download_dir, downloaded_files[0])

#         # Save a copy to the main Downloads folder
#         shutil.copy(file_to_send, os.path.join(MAIN_DOWNLOAD_FOLDER, os.path.basename(file_to_send)))

#         # Trigger native browser download
#         response = FileResponse(
#             open(file_to_send, 'rb'),
#             as_attachment=True,
#             filename=os.path.basename(file_to_send),
#             content_type='application/octet-stream'
#         )
#         return response

#     except instaloader.exceptions.ConnectionException as e:
#         return JsonResponse({'error': 'Connection issue with Instagram'}, status=503)
#     except instaloader.exceptions.InvalidArgumentException:
#         return JsonResponse({'error': 'Invalid Instagram content'}, status=400)
#     except Exception as e:
#         logger.exception(f"Unexpected error: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500)


# import os
# import shutil
# import instaloader
# import time
# import uuid
# import re
# from urllib.parse import urlparse
# from django.http import FileResponse, JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings

# # Define your system Downloads folder:
# MAIN_DOWNLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# def index(request):
#     return render(request, 'index.html')

# def get_unique_download_dir():
#     unique_dir = os.path.join(settings.MEDIA_ROOT, 'downloads', str(uuid.uuid4()))
#     os.makedirs(unique_dir, exist_ok=True)
#     return unique_dir

# def validate_url(url):
#     return re.match(r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)", url) is not None

# def extract_shortcode(url):
#     parsed_url = urlparse(url)
#     parts = parsed_url.path.strip('/').split('/')
#     if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
#         return parts[1]
#     return None

# @csrf_exempt
# def download_content(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
#     try:
#         url = request.POST.get('url', '').strip()
#         if not url:
#             return JsonResponse({'error': 'No URL provided'}, status=400)
#         if not validate_url(url):
#             return JsonResponse({'error': 'Invalid URL'}, status=400)

#         shortcode = extract_shortcode(url)
#         if not shortcode:
#             return JsonResponse({'error': 'Could not extract shortcode'}, status=400)

#         download_dir = get_unique_download_dir()

#         # Use Instaloader to download the post.
#         L = instaloader.Instaloader(download_video_thumbnails=False, save_metadata=False)
#         post = instaloader.Post.from_shortcode(L.context, shortcode)
#         L.download_post(post, target=download_dir)

#         # Wait until file(s) appear.
#         retries = 5
#         for _ in range(retries):
#             downloaded_files = [f for f in os.listdir(download_dir) if f.lower().endswith(('.mp4', '.jpg', '.jpeg', '.png'))]
#             if downloaded_files:
#                 break
#             time.sleep(0.5)
#         if not downloaded_files:
#             return JsonResponse({'error': 'No downloadable content found'}, status=404)

#         file_to_send = os.path.join(download_dir, downloaded_files[0])

#         # Copy file to the system's Downloads folder.
#         destination_path = os.path.join(MAIN_DOWNLOAD_FOLDER, downloaded_files[0])
#         shutil.copy(file_to_send, destination_path)

#         # Return a FileResponse with proper Content-Disposition so the browser shows the native download prompt.
#         response = FileResponse(open(file_to_send, 'rb'),
#                                 as_attachment=True,
#                                 filename=os.path.basename(file_to_send))
#         response['Content-Length'] = os.path.getsize(file_to_send)
#         return response

#     except Exception as e:
#         return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

import os
import instaloader
import time
import uuid
import re
from urllib.parse import urlparse
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# This folder is on your server.
MAIN_DOWNLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

def index(request):
    return render(request, 'index.html')

def get_unique_download_dir():
    unique_id = str(uuid.uuid4())
    unique_dir = os.path.join(settings.MEDIA_ROOT, 'downloads', unique_id)
    os.makedirs(unique_dir, exist_ok=True)
    return unique_dir

def validate_url(url):
    # Validate Instagram URLs (posts, reels, tv)
    return re.match(r"(https?://www\.instagram\.com/(p|reel|tv)/[A-Za-z0-9_-]+)", url) is not None

def extract_shortcode(url):
    parsed_url = urlparse(url)
    parts = parsed_url.path.strip('/').split('/')
    if len(parts) >= 2 and parts[0] in ['p', 'reel', 'tv']:
        return parts[1]
    return None

@csrf_exempt
def download_content(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed", status=405)
    try:
        url = request.POST.get('url', '').strip()
        if not url:
            return HttpResponse("No URL provided", status=400)
        if not validate_url(url):
            return HttpResponse("Invalid URL", status=400)
        
        shortcode = extract_shortcode(url)
        if not shortcode:
            return HttpResponse("Could not extract shortcode", status=400)
        
        # Create a unique directory to store the downloaded content
        download_dir = get_unique_download_dir()
        
        # Use Instaloader to download the Instagram post
        L = instaloader.Instaloader(download_video_thumbnails=False, save_metadata=False)
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=download_dir)
        
        # Wait for the file(s) to appear (try up to 20 seconds)
        retries = 20
        downloaded_files = []
        for _ in range(retries):
            downloaded_files = [
                f for f in os.listdir(download_dir)
                if f.lower().endswith(('.mp4', '.jpg', '.jpeg', '.png'))
            ]
            if downloaded_files:
                break
            time.sleep(1)
        if not downloaded_files:
            return HttpResponse("No downloadable content found", status=404)
        
        # Use the first file found
        file_to_send = os.path.join(download_dir, downloaded_files[0])
        
        # (Optional) Copy the file to your server's MAIN_DOWNLOAD_FOLDER.
        # Note: This copy occurs on the server and does not affect the client's save location.
        try:
            destination_path = os.path.join(MAIN_DOWNLOAD_FOLDER, downloaded_files[0])
            # Uncomment the next line if you wish to keep a server-side copy.
            # shutil.copy(file_to_send, destination_path)
        except Exception as copy_err:
            print("Error copying file:", copy_err)
        
        # Return a FileResponse to trigger the browser’s download (Content-Disposition forces attachment)
        response = FileResponse(
            open(file_to_send, 'rb'),
            as_attachment=True,
            filename=os.path.basename(file_to_send)
        )
        response['Content-Length'] = os.path.getsize(file_to_send)
        return response

    except Exception as e:
        return HttpResponse(f"Unexpected error: {str(e)}", status=500)



