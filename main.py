use_UI = False

if __name__ == '__main__':
    if use_UI == True:
        import UI
        UI.main()
    else:
        import CLApp
        CLApp.main()
