from flask import Flask, request
from trafilatura import fetch_url, extract

app = Flask(__name__)


@app.route('/api/v1/process', methods=['GET'])
def process_url():
    url_to_scrape = request.args.get('url')

    if not url_to_scrape:
        return 'No url provided', 400

    try:
        scrape_result = fetch_url(url_to_scrape)
    except Exception as error:
        print(error)
        return 'Unable to read url', 500

    if not scrape_result:
        return 'Unable to prase url', 500

    return extract(scrape_result, output_format='json'), 200


if __name__ == '__main__':
    app.run()
