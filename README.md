# Prismatic.io to CircleCI webhook

As the prismic.io webhook cannot send data only secret we need a tool to change branches.


## TO INSTALL

- install serverless framework
- setup AWS CLI
- setup AWS Profile
- Get personal token from CircleCI
- edit serverless.yml profile to use correct AWS profile
- copy env.yml.example to env.yml file
- Add CircleCI personal api token into env.yml
- Add correct CircleCI url into env.yml (See https://circleci.com/docs/api/v1-reference/)
- Create a secret string and copy it to env.yml as secret_token
- serverless deploy
- Add api endpoint to prismic.io webhook
- Add secret_token to prismic.io webhook
