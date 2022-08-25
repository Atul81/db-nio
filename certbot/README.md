## Let's Encrypt Using NGINX and Certbot

[Blog](https://mindsers.blog/post/https-using-nginx-certbot-docker)

```bash
# get certificates
$ docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.org

# renew
$ docker compose run --rm certbot renew
```