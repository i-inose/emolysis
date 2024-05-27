from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TextInputForm
from .forms import SignUpForm
from .utils import analyze_sentiment

@login_required
def analyze_text(request):
  if request.method == "POST":
    form = TextInputForm(request.POST)
    if form.is_valid():
      text_input = form.save()
      label, score = analyze_sentiment(text_input.text)
      context = {
				"form": form,
				"label": label,
				"score": score,
				"text": text_input.text
			}
      return render(request, "analysis/result.html", context)
  else:
    form = TextInputForm()
  return render(request, "analysis/index.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('analyze_text')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})