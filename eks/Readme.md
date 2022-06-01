command :

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 176352050582.dkr.ecr.us-east-1.amazonaws.com

aws ecr create-repository \
    --repository-name {NOM} \
    --image-scanning-configuration scanOnPush=true \
    --region us-east-1 


docker build -t {NOM} .

docker tag myapiback2:latest 176352050582.dkr.ecr.us-east-1.amazonaws.com/{NOM}:latest

docker push 176352050582.dkr.ecr.us-east-1.amazonaws.com/{NOM}:latest

docker pull 176352050582.dkr.ecr.us-east-1.amazonaws.com/{NOM}:latest