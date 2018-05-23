def main():
    from surveyapi.app import create_app
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()