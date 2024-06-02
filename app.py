from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
def home():
   
    today_day_of_week = datetime.today().strftime('%A')
    tomorrow_date = datetime.today() + timedelta(days=1)
    tomorrow_day_of_week = tomorrow_date.strftime('%A')
    
    today_day_of_week = datetime.today().strftime('%A')
    members = Member.query.all()
   
    tasks = Task.query.filter_by(day_of_week=today_day_of_week)
    weekend_tasks = WeekendTask.query.all()
    w_t_t = WeekendTask.query.filter_by(day_of_week=tomorrow_day_of_week)
    menu = Menu.query.filter_by(day_of_week=today_day_of_week)
    menu_tomorrow = Menu.query.filter_by(day_of_week=tomorrow_day_of_week)
    return render_template('home.html', members=members, tasks=tasks, weekend_tasks=weekend_tasks, menu=menu, menu_tomorrow=menu_tomorrow, w_t_t=w_t_t)

# Create database tables and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
