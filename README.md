# MelodyMap

MelodyMap is an online map where you can find musicians that are looking to join a band and vice versa. Through MelodyMap, musicians can easily connect with other musicians that live near them.

## Getting Started

These instructions will get this running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
* Node v11.14.0
* NPM 6.9.0
* Python 3.7.x
```

### Installing

There are two environments that you need to set up to be able to get this running on your localhost. One is using Vue (Nuxt) and the other one is using Django. 

#### Install and run Django

```
virtualenv .env
source .env/bin/active
pip install -r requirements.txt
cd back
python manage.py migrate
python manage.py loaddata adverts/fixtures/instruments.json
python manage.py createsuperuser
ENV_PATH=back/.env.example python manage.py runserver
```
Alternatively, you can rename `.env.example` to `.env` and then you can remove the `ENV_PATH=back/.env.example` in the last command.

#### Install and run Nuxt

```
cd front
npm install
npm run dev
```

## Deployment

There are many ways to deploy this on your own system. Heroku is probably the easiest way to get it live. The master branch on this repo is connected to an Heroku project and will be deployed automatically through continous integration. Therefore, the master branch will always be the same as what is running on the server.

If you want to get it running on Heroku, then you will only have to fill in the environment variables and connect the repo to a new Heroku project.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

See the list of [contributors](https://github.com/GDay/MelodyMap/graphs/contributors).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details