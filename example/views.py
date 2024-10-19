from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from django.urls import reverse  # For generating the URL
from example.news_sources import scrape_all_news  # Ensure the path is correct
import datetime

# Home view that shows a welcome message and a button to scrape news
def home_view(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Scrape News</title>
            </head>
            <body>
                <h1>Welcome to the News Scraper</h1>
                <p>To scrape the news, click the button below:</p>
                <form method="get" action="articles/scrape-news/">
                    <button type="submit" name="scrape">Scrape News</button>
                </form>
            </body>
        </html>
    """)

@require_GET
def scrape_view(request):
    try:
        # Get the current date
        current_date = datetime.datetime.now().date()
       
        
        # Call the scraping function to fetch the news articles
        news = scrape_all_news(current_date)

        # Check if any news articles were found
        if not news:
            # Return a JSON response with 204 status code (No Content) if no articles are scraped
            return JsonResponse({'message': f"No articles found for {current_date}."}, status=204)

        # Return the scraped news articles as a JSON response
        return JsonResponse(news, status=200)

    except Exception as e:
        # Log the exception and return a 500 response with the error message
        print(f"Error occurred during scraping: {e}")
        return JsonResponse({
            'error': 'An error occurred during the scraping process.',
            'details': str(e)
        }, status=500)
