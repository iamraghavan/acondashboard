import uuid
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from .firebase_config import auth, db, storage
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt


from uuid import uuid4
from datetime import datetime

# In-memory storage for login attempts (use a database or cache for production)
login_attempts = {}

def login_page(request):
    if request.session.get('uid'):
        return redirect('dashboard_page', unique_id=request.session['unique_id'])
    return render(request, 'auth/login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)    
            request.session['uid'] = user['idToken']  # Use 'idToken' instead of 'localId'
            request.session['email'] = user['email']
            unique_id = uuid.uuid4().hex
            request.session['unique_id'] = unique_id
            return redirect('dashboard_page', unique_id=unique_id)
        except Exception as e:
            error_message = str(e)
            return render(request, 'auth/login.html', {'error': error_message})
    return render(request, 'auth/login.html')

def dashboard(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return redirect('login_page')
    context = {
        'title': 'Dashboard',
        'breadcrumbs_title': 'Dashboard',
        'email': request.session.get('email', 'Unknown'),
    }
    return render(request, 'pages/dashboard.html', context)

def events_page(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return redirect('login_page')

    user_id_token = request.session.get('uid')

    try:
        events = db.child("events").get(user_id_token).val()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    context = {
        'title': 'Events Page - Andavar College of Nursing - Bumble Bees - Admin Dashboard',
        'breadcrumbs_title': 'Events',
        'email': request.session.get('email', 'Unknown'),
        'events': events
    }

    return render(request, 'pages/events.html', context)





def upload_event_image(event_id, image_file):
    filename = str(uuid.uuid4())
    storage.child(f"event_images/{event_id}/{filename}").put(image_file)
    return storage.child(f"event_images/{event_id}/{filename}").get_url(None)


@require_POST
def create_event(request, unique_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        location = request.POST.get('location')
        created_by = request.POST.get('created_by')
        image_file = request.FILES.get('event_image')

        # Validate and process image file if provided
        image_url = ""
        if image_file:
            # Validate file extension and size
            if not image_file.name.lower().endswith('.webp'):
                return JsonResponse({'error': 'Please upload a .webp file.'}, status=400)
            
            # Process image upload
            image_url = upload_event_image(unique_id, image_file)

        try:
            # Generate unique event ID and save event data
            event_id = f"acon-event-{str(uuid4().hex)[:8]}" 
            created_timestamp = datetime.now().isoformat()

            event_data = {
                'event_id': event_id,
                'title': title,
                'description': description,
                'date': date,
                'location': location,
                'created_by': created_by,
                'image_url': image_url if image_url else "",  # Set image_url to empty string if not uploaded
                'created_timestamp': created_timestamp
            }

            event_ref = db.child("events").child(event_id).set(event_data)

            return JsonResponse({'message': 'Event created successfully.', 'event_id': event_id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed.'}, status=405)




@csrf_exempt 
@require_POST
def delete_event(request, event_id):
    try:
        # Delete event data from Firebase Realtime Database
        db.child("events").child(event_id).remove()

        # Delete associated image from Firebase Storage
        image_url = db.child("events").child(event_id).child("image_url").get().val()
        if image_url:
            storage_ref = storage.child(image_url)
            storage_ref.delete()

        return JsonResponse({'message': 'Event deleted successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def view_event(request, event_id):
    try:
        # Retrieve event details from Firebase Realtime Database
        event_data = db.child("events").child(event_id).get().val()
        if not event_data:
            raise Http404("Event does not exist")

        # Prepare context with event details
        context = {
            'event': event_data,
            'title': 'Event Details'  # Customize title as needed
        }

        return JsonResponse(event_data)
        # return render(request, 'pages/event_details.html', context)
    except Exception as e:
        raise Http404("Event does not exist")
    
    
def update_event(request, event_id):
    if request.method == 'POST':
        try:
            event_data = json.loads(request.body)

            # Update event data in Firebase Realtime Database
            event_ref = db.child("events").child(event_id)
            event_ref.update(event_data)

            return JsonResponse({'message': 'Event updated successfully.', 'event_id': event_id})
        except KeyError as e:
            return JsonResponse({'error': f'Missing key in event data: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    





def circulars_page(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return redirect('login_page')

    user_id_token = request.session.get('uid')

    try:
        circular_data = db.child("circulars").get(user_id_token).val()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    context = {
        'title': 'Circular Page - Andavar College of Nursing - Bumble Bees - Admin Dashboard',
        'breadcrumbs_title': 'Circular',
        'email': request.session.get('email', 'Unknown'),
        'circulars': circular_data
    }

    return render(request, 'pages/circulars.html', context)


def view_circular(request, circular_id):
    circular = db.child("circulars").child(circular_id).get().val()
    return JsonResponse({'circular': circular})

@csrf_exempt
def delete_circular(request, id):
    if request.method == 'DELETE':
        db.child("circulars").child(id).remove()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def get_circular(request, id):
    circular = db.child("circulars").child(id).get().val()
    return JsonResponse({'circular': circular})

@csrf_exempt
def edit_circular(request, id):
    if request.method == 'POST':
        try:
            circular_data = request.POST
            circular_ref = db.child("circulars").child(id)
            circular_ref.update(circular_data)
            return JsonResponse({'success': True, 'circular_id': id})
        except KeyError as e:
            return JsonResponse({'error': f'Missing key in circular data: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

@csrf_exempt
def create_circular(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        circular_pdf = request.FILES.get('circular_pdf')
        date = request.POST.get('date')
        location = request.POST.get('location')
        authorized_person = request.POST.get('authorized_person')

        circular_id = f"acon-circular-{str(uuid.uuid4().hex)[:8]}"
        created_timestamp = datetime.now().isoformat()

        pdf_url = ""

        if circular_pdf:
            try:
                # Upload PDF file to Firebase Storage
                pdf_file = storage.child("circulars/" + circular_pdf.name).put(circular_pdf)
                pdf_url = storage.child("circulars/" + circular_pdf.name).get_url(pdf_file['downloadTokens'])
            except Exception as e:
                return JsonResponse({'error': f'Failed to upload PDF: {str(e)}'}, status=500)

        circular_data = {
            'circular_id': circular_id,
            'title': title,
            'description': description,
            'date': date,
            'location': location,
            'pdf_url': pdf_url if pdf_url else "",
            'authorized_person': authorized_person,
            'created_timestamp': created_timestamp
        }

        try:
            # Save circular data in Firebase Realtime Database
            db.child("circulars").child(circular_id).set(circular_data)

            return JsonResponse({'success': True, 'message': 'Circular created successfully.', 'circular_id': circular_id})
        except Exception as e:
            return JsonResponse({'error': f'Failed to add circular to database: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Method not allowed.'}, status=405)





def sign_out(request):
    request.session.flush()
    response = redirect('login_page')
    response.delete_cookie('uid')
    response.delete_cookie('email')
    response.delete_cookie('unique_id')
    return response

def debug_view(request):
    print(request.session.get('unique_id'))
    return HttpResponse("Check console for session data.")
