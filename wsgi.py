from restaurant_backend import create_app

app = create_app()

print("Starting server")

if __name__ == '__main__':
    app.run(host='0.0.0.0')