from django.shortcuts import render


def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, "error_pages/400.html", status=400)


def handler403(request, exception):
    """ Error Handler 403 - Forbidden Error """
    return render(request, "error_pages/403.html", status=403)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "error_pages/404.html", status=404)


def handler500(request, exception):
    """ Error Handler 500 - Internal server error """
    return render(request, "error_pages/500.html", status=500)
