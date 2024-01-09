from chalice import Chalice

app = Chalice(app_name='scheduled_lambda')


# Lambda com disparo programado
@app.schedule("cron(0 10 * * * *)")
def scheduled(event):
    return 'Hello from Lambda!'
