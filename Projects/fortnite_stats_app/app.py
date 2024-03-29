from flask import Flask, render_template
import fortnite_api

app = Flask(__name__)

api_key = '<api_key_here>'
api = fortnite_api.FortniteAPI(api_key=api_key)
user = '<user_name>'


def get_stats():
    account = api.stats.fetch_by_name(name=user)
    raw_data = account.stats.all.raw_data

    stats = {
        "user": account.user.name,
        "battle_pass_level": account.battle_pass.level,
        "overall": raw_data['overall'],
        "solo": raw_data['solo'],
        "duo": raw_data['duo'],
        "squad": raw_data['squad']
    }
    return stats


@app.route('/')
def index():
    stats = get_stats()
    return render_template('index.html', stats=stats)


if __name__ == '__main__':
    app.run()
