After resolving some issues with getting the Flagsmith environment variables to the CI actions, I encountered a new issue in the deployment phase during the docker image build step. For each run I have listed the logs in a collapsable field if you would like to take a look.


**Step**: Build Docker Image\
**Result**: [Errno 28] No space left on device.
<details><summary>Deployment run 1 log</summary>

    ======CMD======
    docker build --pull -t book_store:latest ~/book_store

    ======END======
    err: #0 building with "default" instance using docker driver
    err: #1 [internal] load build definition from Dockerfile
    err: #1 transferring dockerfile: 285B done
    err: #1 DONE 0.0s
    err: #2 [internal] load metadata for docker.io/library/ python:3.13
    err: #2 DONE 0.8s
    err: #3 [internal] load .dockerignore
    err: #3 transferring context: 2B done
    err: #3 DONE 0.0s
    err: #4 [1/4] FROM docker.io/library/python:3.  13@sha256:6a9220edda062e9223ea0784740a535987299420b96fbfd520b8    9bbd3e772485
    err: #4 resolve docker.io/library/python:3. 13@sha256:6a9220edda062e9223ea0784740a535987299420b96fbfd520b8   9bbd3e772485 0.0s done
    err: #4 DONE 0.0s
    err: #5 [internal] load build context
    err: #5 transferring context: 523.21kB 0.2s done
    err: #5 DONE 0.2s
    err: #4 [1/4] FROM docker.io/library/python:3.  13@sha256:6a9220edda062e9223ea0784740a535987299420b96fbfd520b8    9bbd3e772485
    err: #4 CACHED
    err: #6 [2/4] COPY . /app
    err: #6 DONE 3.4s
    err: #7 [3/4] WORKDIR /app
    err: #7 DONE 0.1s
    err: #8 [4/4] RUN pip install -r requirements.txt
    err: #8 3.041 Collecting bcrypt==5.0.0 (from -r requirements.   txt (line 1))
    err: #8 3.069   Downloading bcrypt-5.0. 0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
    err: #8 3.093 Collecting blinker==1.9.0 (from -r requirements.  txt (line 2))
    err: #8 3.097   Downloading blinker-1.9.0-py3-none-any.whl. metadata (1.6 kB)
    err: #8 3.121 Collecting certifi==2026.10.23 (from -r   requirements.txt (line 3))
    err: #8 3.125   Downloading certifi-2026.10.23-py3-none-any.    whl.metadata (2.5 kB)
    err: #8 3.272 Collecting charset-normalizer==3.5.2 (from -r     requirements.txt (line 4))
    err: #8 3.277   Downloading charset_normalizer-3.5. 2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.    manylinux_2_28_x86_64.whl.metadata (46 kB)
    err: #8 3.309 Collecting click==8.5.0 (from -r requirements.    txt (line 5))
    err: #8 3.313   Downloading click-8.5.0-py3-none-any.whl.   metadata (2.6 kB)
    err: #8 3.411 Collecting flagsmith==6.3.0 (from -r  requirements.txt (line 6))
    err: #8 3.417   Downloading flagsmith-6.3.0-py3-none-any.whl.   metadata (2.1 kB)
    err: #8 3.517 Collecting flagsmith-flag-engine==11.1.1 (from    -r requirements.txt (line 7))
    err: #8 3.524   Downloading flagsmith_flag_engine-11.1. 1-py3-none-any.whl.metadata (1.8 kB)
    err: #8 3.546 Collecting Flask==3.1.3 (from -r requirements.    txt (line 8))
    err: #8 3.553   Downloading flask-3.1.3-py3-none-any.whl.   metadata (3.2 kB)
    err: #8 3.572 Collecting Flask-Bcrypt==1.0.1 (from -r   requirements.txt (line 9))
    err: #8 3.577   Downloading Flask_Bcrypt-1.0.1-py3-none-any.    whl.metadata (2.6 kB)
    err: #8 3.755 Collecting greenlet==3.5.6 (from -r   requirements.txt (line 10))
    err: #8 3.760   Downloading greenlet-3.5.   6-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl. metadata (3.8 kB)
    err: #8 3.785 Collecting idna==3.20 (from -r requirements.txt   (line 11))
    err: #8 3.790   Downloading idna-3.20-py3-none-any.whl. metadata (7.2 kB)
    err: #8 3.810 Collecting iniconfig==2.3.1 (from -r  requirements.txt (line 12))
    err: #8 3.814   Downloading iniconfig-2.3.1-py3-none-any.whl.   metadata (2.8 kB)
    err: #8 3.926 Collecting iregexp-check==0.1.4 (from -r  requirements.txt (line 13))
    err: #8 4.006   Downloading iregexp_check-0.1.  4-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.   metadata (2.3 kB)
    err: #8 4.025 Collecting itsdangerous==2.2.0 (from -r   requirements.txt (line 14))
    err: #8 4.029   Downloading itsdangerous-2.2.0-py3-none-any.    whl.metadata (1.9 kB)
    err: #8 4.051 Collecting Jinja2==3.1.6 (from -r requirements.   txt (line 15))
    err: #8 4.055   Downloading jinja2-3.1.6-py3-none-any.whl.  metadata (2.9 kB)
    err: #8 4.151 Collecting jsonpath-rfc9535==0.2.0 (from -r   requirements.txt (line 16))
    err: #8 4.162   Downloading jsonpath_rfc9535-0.2.   0-py3-none-any.whl.metadata (8.3 kB)
    err: #8 4.233 Collecting MarkupSafe==3.0.4 (from -r     requirements.txt (line 17))
    err: #8 4.238   Downloading markupsafe-3.0. 4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.    manylinux_2_28_x86_64.whl.metadata (2.7 kB)
    err: #8 4.261 Collecting packaging==26.3 (from -r   requirements.txt (line 18))
    err: #8 4.265   Downloading packaging-26.3-py3-none-any.whl.    metadata (3.5 kB)
    err: #8 4.315 Collecting playwright==1.64.1 (from -r    requirements.txt (line 19))
    err: #8 4.320   Downloading playwright-1.64.    1-py3-none-manylinux1_x86_64.whl.metadata (3.3 kB)
    err: #8 4.339 Collecting pluggy==1.7.0 (from -r requirements.   txt (line 20))
    err: #8 4.343   Downloading pluggy-1.7.0-py3-none-any.whl.  metadata (5.0 kB)
    err: #8 4.366 Collecting psycopg==3.3.6 (from -r requirements.  txt (line 21))
    err: #8 4.370   Downloading psycopg-3.3.6-py3-none-any.whl. metadata (4.4 kB)
    err: #8 4.394 Collecting pyee==14.0.0 (from -r requirements.    txt (line 22))
    err: #8 4.399   Downloading pyee-14.0.0-py3-none-any.whl.   metadata (1.8 kB)
    err: #8 4.424 Collecting Pygments==2.21.0 (from -r  requirements.txt (line 23))
    err: #8 4.433   Downloading pygments-2.21.0-py3-none-any.whl.   metadata (2.5 kB)
    err: #8 4.467 Collecting pytest==9.1.1 (from -r requirements.   txt (line 24))
    err: #8 4.472   Downloading pytest-9.1.1-py3-none-any.whl.  metadata (7.6 kB)
    err: #8 4.496 Collecting pytest-playwright==0.10.0 (from -r     requirements.txt (line 25))
    err: #8 4.501   Downloading pytest_playwright-0.10. 0-py3-none-any.whl.metadata (14 kB)
    err: #8 4.526 Collecting python-dotenv==1.2.4 (from -r  requirements.txt (line 26))
    err: #8 4.530   Downloading python_dotenv-1.2.4-py3-none-any.   whl.metadata (29 kB)
    err: #8 4.559 Collecting python-slugify==9.1.3 (from -r     requirements.txt (line 27))
    err: #8 4.568   Downloading python_slugify-9.1.3-py3-none-any.  whl.metadata (12 kB)
    err: #8 5.015 Collecting regex==2026.9.29 (from -r  requirements.txt (line 28))
    err: #8 5.019   Downloading regex-2026.9.   29-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64. manylinux_2_28_x86_64.whl.metadata (40 kB)
    err: #8 5.052 Collecting requests==2.34.2 (from -r  requirements.txt (line 29))
    err: #8 5.056   Downloading requests-2.34.2-py3-none-any.whl.   metadata (4.8 kB)
    err: #8 5.074 Collecting requests-futures==1.1.0 (from -r   requirements.txt (line 30))
    err: #8 5.079   Downloading requests_futures-1.1.   0-py3-none-any.whl.metadata (9.5 kB)
    err: #8 5.102 Collecting semver==3.1.0 (from -r requirements.   txt (line 31))
    err: #8 5.106   Downloading semver-3.1.0-py3-none-any.whl.  metadata (6.9 kB)
    err: #8 5.125 Collecting sseclient-py==1.9.0 (from -r   requirements.txt (line 32))
    err: #8 5.129   Downloading sseclient_py-1.9.0-py3-none-any.    whl.metadata (1.9 kB)
    err: #8 5.146 Collecting text-unidecode==1.3 (from -r   requirements.txt (line 33))
    err: #8 5.151   Downloading text_unidecode-1.3-py2. py3-none-any.whl.metadata (2.4 kB)
    err: #8 5.174 Collecting typing_extensions==4.16.0 (from -r     requirements.txt (line 34))
    err: #8 5.178   Downloading typing_extensions-4.16. 0-py3-none-any.whl.metadata (3.3 kB)
    err: #8 5.205 Collecting urllib3==2.8.0 (from -r requirements.  txt (line 35))
    err: #8 5.209   Downloading urllib3-2.8.0-py3-none-any.whl. metadata (7.4 kB)
    err: #8 5.235 Collecting Werkzeug==3.1.9 (from -r   requirements.txt (line 36))
    err: #8 5.240   Downloading werkzeug-3.1.9-py3-none-any.whl.    metadata (4.1 kB)
    err: #8 5.291 Downloading bcrypt-5.0.   0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
    err: #8 5.303 Downloading blinker-1.9.0-py3-none-any.whl (8.5   kB)
    err: #8 5.312 Downloading certifi-2026.10.23-py3-none-any.whl   (135 kB)
    err: #8 5.323 Downloading charset_normalizer-3.5.   2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.  manylinux_2_28_x86_64.whl (254 kB)
    err: #8 5.336 Downloading click-8.5.0-py3-none-any.whl (125     kB)
    err: #8 5.348 Downloading flagsmith-6.3.0-py3-none-any.whl  (22 kB)
    err: #8 5.358 Downloading flagsmith_flag_engine-11.1.   1-py3-none-any.whl (16 kB)
    err: #8 5.369 Downloading jsonpath_rfc9535-0.2.0-py3-none-any.  whl (36 kB)
    err: #8 5.378 Downloading requests-2.34.2-py3-none-any.whl  (73 kB)
    err: #8 5.388 Downloading idna-3.20-py3-none-any.whl (69 kB)
    err: #8 5.399 Downloading requests_futures-1.1.0-py3-none-any.  whl (10 kB)
    err: #8 5.409 Downloading semver-3.1.0-py3-none-any.whl (18     kB)
    err: #8 5.418 Downloading sseclient_py-1.9.0-py3-none-any.whl   (8.4 kB)
    err: #8 5.428 Downloading typing_extensions-4.16.   0-py3-none-any.whl (45 kB)
    err: #8 5.438 Downloading urllib3-2.8.0-py3-none-any.whl (135   kB)
    err: #8 5.452 Downloading flask-3.1.3-py3-none-any.whl (103     kB)
    err: #8 5.467 Downloading Flask_Bcrypt-1.0.1-py3-none-any.whl   (6.0 kB)
    err: #8 5.480 Downloading greenlet-3.5. 6-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl    (623 kB)
    err: #8 5.492    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 623.  8/623.8 kB 42.3 MB/s  0:00:00
    err: #8 5.496 Downloading iniconfig-2.3.1-py3-none-any.whl (7.  6 kB)
    err: #8 5.507 Downloading iregexp_check-0.1.    4-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl  (250 kB)
    err: #8 5.519 Downloading itsdangerous-2.2.0-py3-none-any.whl   (16 kB)
    err: #8 5.529 Downloading jinja2-3.1.6-py3-none-any.whl (134    kB)
    err: #8 5.539 Downloading markupsafe-3.0.   4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.  manylinux_2_28_x86_64.whl (23 kB)
    err: #8 5.549 Downloading packaging-26.3-py3-none-any.whl   (129 kB)
    err: #8 5.560 Downloading playwright-1.64.  1-py3-none-manylinux1_x86_64.whl (48.5 MB)
    err: #8 5.835    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.   5/48.5 MB 178.2 MB/s  0:00:00
    err: #8 5.841 Downloading pyee-14.0.0-py3-none-any.whl (15 kB)
    err: #8 5.849 Downloading pluggy-1.7.0-py3-none-any.whl (27     kB)
    err: #8 5.859 Downloading psycopg-3.3.6-py3-none-any.whl (215   kB)
    err: #8 5.870 Downloading pygments-2.21.0-py3-none-any.whl (1.  3 MB)
    err: #8 5.883    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/  1.3 MB 100.7 MB/s  0:00:00
    err: #8 5.887 Downloading pytest-9.1.1-py3-none-any.whl (386    kB)
    err: #8 5.901 Downloading pytest_playwright-0.10.   0-py3-none-any.whl (22 kB)
    err: #8 5.911 Downloading python_slugify-9.1.3-py3-none-any.    whl (16 kB)
    err: #8 5.921 Downloading python_dotenv-1.2.4-py3-none-any. whl (23 kB)
    err: #8 5.932 Downloading regex-2026.9. 29-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.   manylinux_2_28_x86_64.whl (807 kB)
    err: #8 5.944    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.  9/807.9 kB 61.0 MB/s  0:00:00
    err: #8 5.949 Downloading text_unidecode-1.3-py2.py3-none-any.  whl (78 kB)
    err: #8 5.960 Downloading werkzeug-3.1.9-py3-none-any.whl   (228 kB)
    err: #8 6.440 Installing collected packages: text-unidecode,    urllib3, typing_extensions, sseclient-py, semver, regex,   python-slugify, python-dotenv, Pygments, psycopg, pluggy,     packaging, MarkupSafe, itsdangerous, iregexp-check,     iniconfig, idna, greenlet, click, charset-normalizer,   certifi, blinker, bcrypt, Werkzeug, requests, pytest, pyee,   jsonpath-rfc9535, Jinja2, requests-futures, playwright,   Flask, flagsmith-flag-engine, pytest-playwright,  Flask-Bcrypt, flagsmith
    err: #8 9.140 ERROR: Could not install packages due to an   OSError: [Errno 28] No space left on device
    err: #8 9.140 
    err: #8 9.141 
    err: #8 ERROR: process "/bin/sh -c pip install -r   requirements.txt" did not complete successfully: exit code: 1
    err: ------
    err:  > [4/4] RUN pip install -r requirements.txt:
    err: 5.539 Downloading markupsafe-3.0.  4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64. manylinux_2_28_x86_64.whl (23 kB)
    err: 5.549 Downloading packaging-26.3-py3-none-any.whl (129     kB)
    err: 5.560 Downloading playwright-1.64. 1-py3-none-manylinux1_x86_64.whl (48.5 MB)
    err: 5.949 Downloading text_unidecode-1.3-py2.py3-none-any. whl (78 kB)
    err: 5.960 Downloading werkzeug-3.1.9-py3-none-any.whl (228     kB)
    err: 6.440 Installing collected packages: text-unidecode,   urllib3, typing_extensions, sseclient-py, semver, regex,  python-slugify, python-dotenv, Pygments, psycopg, pluggy,    packaging, MarkupSafe, itsdangerous, iregexp-check,    iniconfig, idna, greenlet, click, charset-normalizer,  certifi, blinker, bcrypt, Werkzeug, requests, pytest, pyee,  jsonpath-rfc9535, Jinja2, requests-futures, playwright,  Flask, flagsmith-flag-engine, pytest-playwright,     Flask-Bcrypt, flagsmith
    err: 9.140 ERROR: Could not install packages due to an  OSError: [Errno 28] No space left on device
    err: 9.140 
    err: 9.141 
    err: ------
    err: Dockerfile:6
    err: --------------------
    err:    4 |     COPY . /app
    err:    5 |     WORKDIR /app
    err:    6 | >>> RUN pip install -r requirements.txt
    err:    7 |     CMD ["python", "app.py"]
    err:    8 |     
    err: --------------------
    err: ERROR: failed to solve: process "/bin/sh -c pip install    -r requirements.txt" did not complete successfully: exit   code: 1
    2026/10/30 16:57:28 Process exited with status 1
</details>


From this information, it seems that the instance has run out of space, potentially due to the size of some of the packages required.

After being provided with a space upgrade on my instance (thanks Kerry!), lets look at what happened on my next attempt.


**Step**: Copy app to EC2\
**Result**: Timeout
<details><summary>Deployment run 2 log</summary>

    tar all files into /tmp/YjSMDVLCgP.tar.gz
    scp file to server.
    drone-scp error:  error copy file to dest: ***, error message: dial tcp ***:22: i/o timeout

    2026/10/30 17:10:07 error copy file to dest: ***, error message: dial tcp ***:22: i/o timeout
</details>

This was simply a matter of not updating the EC2_HOST env variable after having my instance upgraded. Ater the upgrade the ip address of the instance changed so this should be updated.


**Step**: Build Docker Image\
**Result**: [Errno 28] No space left on device.
<details><summary>Deplyoment run 3 log</summary>

    ======CMD======
    docker build --pull -t book_store:latest ~/book_store

    ======END======
    err: #0 building with "default" instance using docker driver
    err: #1 [internal] load build definition from Dockerfile
    err: #1 transferring dockerfile: 285B done
    err: #1 DONE 0.0s
    err: #2 [internal] load metadata for docker.io/library/ python:3.13
    err: #2 DONE 0.6s
    err: #3 [internal] load .dockerignore
    err: #3 transferring context: 2B done
    err: #3 DONE 0.0s
    err: #4 [1/4] FROM docker.io/library/python:3.  13@sha256:6a9220edda062e9223ea0784740a535987299420b96fbfd520b8    9bbd3e772485
    err: #4 resolve docker.io/library/python:3. 13@sha256:6a9220edda062e9223ea0784740a535987299420b96fbfd520b8   9bbd3e772485 0.0s done
    err: #4 DONE 0.0s
    err: #5 [internal] load build context
    err: #5 transferring context: 523.21kB 0.3s done
    err: #5 DONE 0.4s
    err: #6 [2/4] COPY . /app
    err: #6 CACHED
    err: #7 [3/4] WORKDIR /app
    err: #7 CACHED
    err: #8 [4/4] RUN pip install -r requirements.txt
    err: #8 2.737 Collecting bcrypt==5.0.0 (from -r requirements.   txt (line 1))
    err: #8 2.770   Downloading bcrypt-5.0. 0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
    err: #8 2.800 Collecting blinker==1.9.0 (from -r requirements.  txt (line 2))
    err: #8 2.805   Downloading blinker-1.9.0-py3-none-any.whl. metadata (1.6 kB)
    err: #8 2.832 Collecting certifi==2026.10.23 (from -r   requirements.txt (line 3))
    err: #8 2.837   Downloading certifi-2026.10.23-py3-none-any.    whl.metadata (2.5 kB)
    err: #8 2.990 Collecting charset-normalizer==3.5.2 (from -r     requirements.txt (line 4))
    err: #8 2.994   Downloading charset_normalizer-3.5. 2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.    manylinux_2_28_x86_64.whl.metadata (46 kB)
    err: #8 3.027 Collecting click==8.5.0 (from -r requirements.    txt (line 5))
    err: #8 3.032   Downloading click-8.5.0-py3-none-any.whl.   metadata (2.6 kB)
    err: #8 3.058 Collecting flagsmith==6.3.0 (from -r  requirements.txt (line 6))
    err: #8 3.066   Downloading flagsmith-6.3.0-py3-none-any.whl.   metadata (2.1 kB)
    err: #8 3.096 Collecting flagsmith-flag-engine==11.1.1 (from    -r requirements.txt (line 7))
    err: #8 3.103   Downloading flagsmith_flag_engine-11.1. 1-py3-none-any.whl.metadata (1.8 kB)
    err: #8 3.128 Collecting Flask==3.1.3 (from -r requirements.    txt (line 8))
    err: #8 3.133   Downloading flask-3.1.3-py3-none-any.whl.   metadata (3.2 kB)
    err: #8 3.156 Collecting Flask-Bcrypt==1.0.1 (from -r   requirements.txt (line 9))
    err: #8 3.161   Downloading Flask_Bcrypt-1.0.1-py3-none-any.    whl.metadata (2.6 kB)
    err: #8 3.363 Collecting greenlet==3.5.6 (from -r   requirements.txt (line 10))
    err: #8 3.368   Downloading greenlet-3.5.   6-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl. metadata (3.8 kB)
    err: #8 3.394 Collecting idna==3.20 (from -r requirements.txt   (line 11))
    err: #8 3.398   Downloading idna-3.20-py3-none-any.whl. metadata (7.2 kB)
    err: #8 3.419 Collecting iniconfig==2.3.1 (from -r  requirements.txt (line 12))
    err: #8 3.423   Downloading iniconfig-2.3.1-py3-none-any.whl.   metadata (2.8 kB)
    err: #8 3.452 Collecting iregexp-check==0.1.4 (from -r  requirements.txt (line 13))
    err: #8 3.457   Downloading iregexp_check-0.1.  4-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.   metadata (2.3 kB)
    err: #8 3.478 Collecting itsdangerous==2.2.0 (from -r   requirements.txt (line 14))
    err: #8 3.483   Downloading itsdangerous-2.2.0-py3-none-any.    whl.metadata (1.9 kB)
    err: #8 3.507 Collecting Jinja2==3.1.6 (from -r requirements.   txt (line 15))
    err: #8 3.511   Downloading jinja2-3.1.6-py3-none-any.whl.  metadata (2.9 kB)
    err: #8 3.533 Collecting jsonpath-rfc9535==0.2.0 (from -r   requirements.txt (line 16))
    err: #8 3.539   Downloading jsonpath_rfc9535-0.2.   0-py3-none-any.whl.metadata (8.3 kB)
    err: #8 3.618 Collecting MarkupSafe==3.0.4 (from -r     requirements.txt (line 17))
    err: #8 3.623   Downloading markupsafe-3.0. 4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.    manylinux_2_28_x86_64.whl.metadata (2.7 kB)
    err: #8 3.649 Collecting packaging==26.3 (from -r   requirements.txt (line 18))
    err: #8 3.654   Downloading packaging-26.3-py3-none-any.whl.    metadata (3.5 kB)
    err: #8 3.716 Collecting playwright==1.64.1 (from -r    requirements.txt (line 19))
    err: #8 3.731   Downloading playwright-1.64.    1-py3-none-manylinux1_x86_64.whl.metadata (3.3 kB)
    err: #8 3.754 Collecting pluggy==1.7.0 (from -r requirements.   txt (line 20))
    err: #8 3.761   Downloading pluggy-1.7.0-py3-none-any.whl.  metadata (5.0 kB)
    err: #8 3.791 Collecting psycopg==3.3.6 (from -r requirements.  txt (line 21))
    err: #8 3.795   Downloading psycopg-3.3.6-py3-none-any.whl. metadata (4.4 kB)
    err: #8 3.825 Collecting pyee==14.0.0 (from -r requirements.    txt (line 22))
    err: #8 3.830   Downloading pyee-14.0.0-py3-none-any.whl.   metadata (1.8 kB)
    err: #8 3.862 Collecting Pygments==2.21.0 (from -r  requirements.txt (line 23))
    err: #8 3.867   Downloading pygments-2.21.0-py3-none-any.whl.   metadata (2.5 kB)
    err: #8 3.909 Collecting pytest==9.1.1 (from -r requirements.   txt (line 24))
    err: #8 3.914   Downloading pytest-9.1.1-py3-none-any.whl.  metadata (7.6 kB)
    err: #8 3.942 Collecting pytest-playwright==0.10.0 (from -r     requirements.txt (line 25))
    err: #8 3.948   Downloading pytest_playwright-0.10. 0-py3-none-any.whl.metadata (14 kB)
    err: #8 3.979 Collecting python-dotenv==1.2.4 (from -r  requirements.txt (line 26))
    err: #8 3.985   Downloading python_dotenv-1.2.4-py3-none-any.   whl.metadata (29 kB)
    err: #8 4.017 Collecting python-slugify==9.1.3 (from -r     requirements.txt (line 27))
    err: #8 4.023   Downloading python_slugify-9.1.3-py3-none-any.  whl.metadata (12 kB)
    err: #8 4.546 Collecting regex==2026.9.29 (from -r  requirements.txt (line 28))
    err: #8 4.551   Downloading regex-2026.9.   29-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64. manylinux_2_28_x86_64.whl.metadata (40 kB)
    err: #8 4.587 Collecting requests==2.34.2 (from -r  requirements.txt (line 29))
    err: #8 4.591   Downloading requests-2.34.2-py3-none-any.whl.   metadata (4.8 kB)
    err: #8 4.613 Collecting requests-futures==1.1.0 (from -r   requirements.txt (line 30))
    err: #8 4.619   Downloading requests_futures-1.1.   0-py3-none-any.whl.metadata (9.5 kB)
    err: #8 4.645 Collecting semver==3.1.0 (from -r requirements.   txt (line 31))
    err: #8 4.650   Downloading semver-3.1.0-py3-none-any.whl.  metadata (6.9 kB)
    err: #8 4.671 Collecting sseclient-py==1.9.0 (from -r   requirements.txt (line 32))
    err: #8 4.681   Downloading sseclient_py-1.9.0-py3-none-any.    whl.metadata (1.9 kB)
    err: #8 4.703 Collecting text-unidecode==1.3 (from -r   requirements.txt (line 33))
    err: #8 4.707   Downloading text_unidecode-1.3-py2. py3-none-any.whl.metadata (2.4 kB)
    err: #8 4.733 Collecting typing_extensions==4.16.0 (from -r     requirements.txt (line 34))
    err: #8 4.737   Downloading typing_extensions-4.16. 0-py3-none-any.whl.metadata (3.3 kB)
    err: #8 4.766 Collecting urllib3==2.8.0 (from -r requirements.  txt (line 35))
    err: #8 4.771   Downloading urllib3-2.8.0-py3-none-any.whl. metadata (7.4 kB)
    err: #8 4.801 Collecting Werkzeug==3.1.9 (from -r   requirements.txt (line 36))
    err: #8 4.806   Downloading werkzeug-3.1.9-py3-none-any.whl.    metadata (4.1 kB)
    err: #8 4.862 Downloading bcrypt-5.0.   0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
    err: #8 4.875 Downloading blinker-1.9.0-py3-none-any.whl (8.5   kB)
    err: #8 4.889 Downloading certifi-2026.10.23-py3-none-any.whl   (135 kB)
    err: #8 4.902 Downloading charset_normalizer-3.5.   2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.  manylinux_2_28_x86_64.whl (254 kB)
    err: #8 4.914 Downloading click-8.5.0-py3-none-any.whl (125     kB)
    err: #8 4.927 Downloading flagsmith-6.3.0-py3-none-any.whl  (22 kB)
    err: #8 4.939 Downloading flagsmith_flag_engine-11.1.   1-py3-none-any.whl (16 kB)
    err: #8 4.951 Downloading jsonpath_rfc9535-0.2.0-py3-none-any.  whl (36 kB)
    err: #8 4.962 Downloading requests-2.34.2-py3-none-any.whl  (73 kB)
    err: #8 4.974 Downloading idna-3.20-py3-none-any.whl (69 kB)
    err: #8 4.987 Downloading requests_futures-1.1.0-py3-none-any.  whl (10 kB)
    err: #8 4.999 Downloading semver-3.1.0-py3-none-any.whl (18     kB)
    err: #8 5.011 Downloading sseclient_py-1.9.0-py3-none-any.whl   (8.4 kB)
    err: #8 5.022 Downloading typing_extensions-4.16.   0-py3-none-any.whl (45 kB)
    err: #8 5.033 Downloading urllib3-2.8.0-py3-none-any.whl (135   kB)
    err: #8 5.044 Downloading flask-3.1.3-py3-none-any.whl (103     kB)
    err: #8 5.056 Downloading Flask_Bcrypt-1.0.1-py3-none-any.whl   (6.0 kB)
    err: #8 5.069 Downloading greenlet-3.5. 6-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl    (623 kB)
    err: #8 5.083    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 623.  8/623.8 kB 40.9 MB/s  0:00:00
    err: #8 5.087 Downloading iniconfig-2.3.1-py3-none-any.whl (7.  6 kB)
    err: #8 5.098 Downloading iregexp_check-0.1.    4-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl  (250 kB)
    err: #8 5.110 Downloading itsdangerous-2.2.0-py3-none-any.whl   (16 kB)
    err: #8 5.120 Downloading jinja2-3.1.6-py3-none-any.whl (134    kB)
    err: #8 5.135 Downloading markupsafe-3.0.   4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.  manylinux_2_28_x86_64.whl (23 kB)
    err: #8 5.146 Downloading packaging-26.3-py3-none-any.whl   (129 kB)
    err: #8 5.174 Downloading playwright-1.64.  1-py3-none-manylinux1_x86_64.whl (48.5 MB)
    err: #8 5.450    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.   5/48.5 MB 176.8 MB/s  0:00:00
    err: #8 5.457 Downloading pyee-14.0.0-py3-none-any.whl (15 kB)
    err: #8 5.468 Downloading pluggy-1.7.0-py3-none-any.whl (27     kB)
    err: #8 5.483 Downloading psycopg-3.3.6-py3-none-any.whl (215   kB)
    err: #8 5.497 Downloading pygments-2.21.0-py3-none-any.whl (1.  3 MB)
    err: #8 5.522    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/  1.3 MB 61.6 MB/s  0:00:00
    err: #8 5.529 Downloading pytest-9.1.1-py3-none-any.whl (386    kB)
    err: #8 5.546 Downloading pytest_playwright-0.10.   0-py3-none-any.whl (22 kB)
    err: #8 5.558 Downloading python_slugify-9.1.3-py3-none-any.    whl (16 kB)
    err: #8 5.567 Downloading python_dotenv-1.2.4-py3-none-any. whl (23 kB)
    err: #8 5.577 Downloading regex-2026.9. 29-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.   manylinux_2_28_x86_64.whl (807 kB)
    err: #8 5.588    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.  9/807.9 kB 77.0 MB/s  0:00:00
    err: #8 5.593 Downloading text_unidecode-1.3-py2.py3-none-any.  whl (78 kB)
    err: #8 5.604 Downloading werkzeug-3.1.9-py3-none-any.whl   (228 kB)
    err: #8 6.058 Installing collected packages: text-unidecode,    urllib3, typing_extensions, sseclient-py, semver, regex,   python-slugify, python-dotenv, Pygments, psycopg, pluggy,     packaging, MarkupSafe, itsdangerous, iregexp-check,     iniconfig, idna, greenlet, click, charset-normalizer,   certifi, blinker, bcrypt, Werkzeug, requests, pytest, pyee,   jsonpath-rfc9535, Jinja2, requests-futures, playwright,   Flask, flagsmith-flag-engine, pytest-playwright,  Flask-Bcrypt, flagsmith
    err: #8 9.216 ERROR: Could not install packages due to an   OSError: [Errno 28] No space left on device
    err: #8 9.216 
    err: #8 9.217 
    err: #8 ERROR: process "/bin/sh -c pip install -r   requirements.txt" did not complete successfully: exit code: 1
    err: ------
    err:  > [4/4] RUN pip install -r requirements.txt:
    err: 5.558 Downloading python_slugify-9.1.3-py3-none-any.whl    (16 kB)
    err: 5.567 Downloading python_dotenv-1.2.4-py3-none-any.whl     (23 kB)
    err: 5.577 Downloading regex-2026.9.    29-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.  manylinux_2_28_x86_64.whl (807 kB)
    err: 5.588    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/   807.9 kB 77.0 MB/s  0:00:00
    err: 5.593 Downloading text_unidecode-1.3-py2.py3-none-any. whl (78 kB)
    err: 5.604 Downloading werkzeug-3.1.9-py3-none-any.whl (228     kB)
    err: 6.058 Installing collected packages: text-unidecode,   urllib3, typing_extensions, sseclient-py, semver, regex,  python-slugify, python-dotenv, Pygments, psycopg, pluggy,    packaging, MarkupSafe, itsdangerous, iregexp-check,    iniconfig, idna, greenlet, click, charset-normalizer,  certifi, blinker, bcrypt, Werkzeug, requests, pytest, pyee,  jsonpath-rfc9535, Jinja2, requests-futures, playwright,  Flask, flagsmith-flag-engine, pytest-playwright,     Flask-Bcrypt, flagsmith
    err: 9.216 ERROR: Could not install packages due to an  OSError: [Errno 28] No space left on device
    err: 9.216 
    err: 9.217 
    err: ------
    err: Dockerfile:6
    err: --------------------
    err:    4 |     COPY . /app
    err:    5 |     WORKDIR /app
    err:    6 | >>> RUN pip install -r requirements.txt
    err:    7 |     CMD ["python", "app.py"]
    err:    8 |     
    err: --------------------
    err: ERROR: failed to solve: process "/bin/sh -c pip install    -r requirements.txt" did not complete successfully: exit   code: 1
    2026/10/30 17:14:46 Process exited with status 1
</details>

Having changed the IP we have now successfully connected again but we seem to have returned to the first errno 28. Is the deployment still too big? Is there a caching or docker issue?

In order to gain some more understanding, I thought it would be good to check for unusually large file sizes on the instance.


**Debug Task**: List all files over 10M on instance\
**Result**: This is too much information for me to understand
<details><summary>List of all files above 10M on my deployment</summary>

    $ sudo find / -type f -size +10M -exec ls -lh {} \;
    -rwxr-xr-x. 1 root root 14M Oct 19 19:42 /boot/vmlinuz-6.18.    56-125.164.amzn2023.x86_64
    -rw-------. 1 root root 21M Oct 23 23:56 /boot/initramfs-6.18.  56-125.164.amzn2023.x86_64.img
    -r--r--r--. 1 root root 12M Oct 23 23:57 /etc/udev/hwdb.bin
    -r--------. 1 root root 128T Oct 30 17:05 /proc/kcore
    find: ‘/proc/3188’: No such file or directory
    find: ‘/proc/3190/task/3190/fdinfo/5’: No such file or  directory
    find: ‘/proc/3190/fdinfo/6’: No such file or directory
    find: ‘/proc/3196’: No such file or directory
    -rw-r--r--. 1 root root 77M Oct 26 15:57 /var/cache/dnf/    amazonlinux-c676dbc499cb0aed/repodata/filelists.xml.gz
    -rw-r--r--. 1 root root 15M Oct 26 16:17 /var/cache/dnf/    amazonlinux.solv
    -rw-r--r--. 1 root root 78M Oct 26 16:17 /var/cache/dnf/    amazonlinux-filenames.solvx
    -rw-r--r--. 1 root root 11M Oct 26 16:17 /var/cache/dnf/    amazonlinux-updateinfo.solvx
    -rw-r--r--. 1 root root 18M Oct 26 16:46 /var/lib/rpm/rpmdb.    sqlite
    -rw-------. 1 systemd-oom systemd-oom 16M Oct 30 17:04 /var/    lib/docker/volumes/ 280949d9668c0ab48a7734638b868c641f865a46f00b50c39f6384effeebbc   c5/_data/pg_wal/000000010000000000000001
    -rw-r--r--. 1 root root 124M Jun 14  2025 /var/lib/docker/  overlay2/ 11f229f35b911f8e630f25d6c309653df1e6a8b0b8472a74cdb6a30ec9cc85   f7/diff/usr/lib/x86_64-linux-gnu/libLLVM.so.19.1
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  11f229f35b911f8e630f25d6c309653df1e6a8b0b8472a74cdb6a30ec9cc85    f7/diff/usr/lib/x86_64-linux-gnu/libicudata.so.76.1
    -rw-r--r--. 1 root root 27M Nov  4  2024 /var/lib/docker/   overlay2/  11f229f35b911f8e630f25d6c309653df1e6a8b0b8472a74cdb6a30ec9cc85    f7/diff/usr/lib/x86_64-linux-gnu/libz3.so.4
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/twc3ae4mb0nzz3utx1eq5w9q6/diff/book_store_venv/lib/  python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 22M Dec 26  2025 /var/lib/docker/   overlay2/  f345e4ba4d01e4709a05a43b54450d83e63d291a637393aecff8a8c1fd6d79    ca/diff/usr/bin/sq
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/bin/x86_64-linux-gnu-lto-dump-14
    -rw-r--r--. 1 root root 11M Mar 15  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/lib/x86_64-linux-gnu/libasan.so.8.0.0
    -rw-r--r--. 1 root root 12M Sep 29 20:10 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/lib/x86_64-linux-gnu/libcrypto.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/lib/x86_64-linux-gnu/libicudata.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/lib/x86_64-linux-gnu/libicudata.so.76.1
    -rwxr-xr-x. 1 root root 33M Mar 15  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/libexec/gcc/x86_64-linux-gnu/14/cc1
    -rwxr-xr-x. 1 root root 35M Mar 15  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/libexec/gcc/x86_64-linux-gnu/14/cc1plus
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  6b2aa750e4c9964ad5eda4018ea3190e4e13f458132ad1e9da2c9d12321397    9e/diff/usr/libexec/gcc/x86_64-linux-gnu/14/lto1
    -rwxr-xr-x. 1 root root 28M Oct 21 22:32 /var/lib/docker/   overlay2/  3332a43c8c4a8a404540d19792c59753dc525c6ef4d60d32d532532f95a4c1    1b/diff/usr/local/lib/libpython3.13.so.1.0
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/haglxcxmmpsdbx8keiajpmrv0/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 26 16:51 /var/lib/docker/  overlay2/vzey3pin3zsu48jum5o5zvwom/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 26 16:50 /var/lib/docker/   overlay2/vzey3pin3zsu48jum5o5zvwom/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 28M Oct 26 22:48 /var/lib/docker/   overlay2/  7649204166d6de570a67cd8225b1bccd57875d2fd2744c425b03de99d65b22    cf/diff/usr/local/lib/libpython3.13.so.1.0
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/x6ikxisph5pwv9lip16y5ski4/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 27 12:24 /var/lib/docker/  overlay2/49e6nr5p4syik5vpx4thvn7ry/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 27 12:24 /var/lib/docker/   overlay2/49e6nr5p4syik5vpx4thvn7ry/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/va7nhbktkk25payskab3dgqku/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 27 15:43 /var/lib/docker/  overlay2/desvhx4tvcb1cb8ne2k39amng/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 27 15:43 /var/lib/docker/   overlay2/desvhx4tvcb1cb8ne2k39amng/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 22M Dec 26  2025 /var/lib/docker/   overlay2/  7c3f2a38fb2bf1ceaa367a664364c777dab6a8a9938af2400f3fbaa444d99a    23/diff/usr/bin/sq
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/bin/x86_64-linux-gnu-lto-dump-14
    -rw-r--r--. 1 root root 11M Mar 15  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/lib/x86_64-linux-gnu/libasan.so.8.0.0
    -rw-r--r--. 1 root root 12M Sep 29 20:10 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/lib/x86_64-linux-gnu/libcrypto.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/lib/x86_64-linux-gnu/libicudata.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/lib/x86_64-linux-gnu/libicudata.so.76.1
    -rwxr-xr-x. 1 root root 33M Mar 15  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/libexec/gcc/x86_64-linux-gnu/14/cc1
    -rwxr-xr-x. 1 root root 35M Mar 15  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/libexec/gcc/x86_64-linux-gnu/14/cc1plus
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  c6e78fcb214506d2cad692c4f0456b7d5b5d47a370dd014fa435287cac0df0    fe/diff/usr/libexec/gcc/x86_64-linux-gnu/14/lto1
    -rwxr-xr-x. 1 root root 28M Oct 28 04:38 /var/lib/docker/   overlay2/  a74cfec40dd9dfe6f9eea645b0370fdd441e878de7823995f398c1bc408fb9    ed/diff/usr/local/lib/libpython3.13.so.1.0
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/yxje4tbk8bj66hx38l86uybgt/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 28 12:14 /var/lib/docker/  overlay2/pb0kqcppgm1s57f6svgkfkjq0/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 28 12:13 /var/lib/docker/   overlay2/pb0kqcppgm1s57f6svgkfkjq0/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/wiyrxhgf1fgtlnz2ya2rt9ihc/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 28 14:42 /var/lib/docker/  overlay2/ldkzjcovrm8qyjez4531d4ze5/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 28 14:42 /var/lib/docker/   overlay2/ldkzjcovrm8qyjez4531d4ze5/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/a60tqoeff52102cr5blphgju2/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 28 14:52 /var/lib/docker/  overlay2/6r6ss8y4muupjvsxefpulfqtc/diff/usr/local/lib/python3.    13/site-packages/playwright/driver/node
    -rw-r--r--. 1 root root 47M Oct 28 14:51 /var/lib/docker/   overlay2/6r6ss8y4muupjvsxefpulfqtc/diff/root/.cache/pip/   http-v2/a/5/b/e/b/ a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rw-r--r--. 1 root root 47M Oct 28 14:51 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/root/.cache/pip/http-v2/a/5/b/e/b/    a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/bin/x86_64-linux-gnu-lto-dump-14
    -rwxr-xr-x. 1 root root 22M Dec 26  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/bin/sq
    -rw-r--r--. 1 root root 11M Mar 15  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/lib/x86_64-linux-gnu/libasan.so.8.0.0
    -rw-r--r--. 1 root root 12M Sep 29 20:10 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/lib/x86_64-linux-gnu/libcrypto.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/lib/x86_64-linux-gnu/libicudata.a
    -rw-r--r--. 1 root root 31M May 31  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/lib/x86_64-linux-gnu/libicudata.so.76.1
    -rwxr-xr-x. 1 root root 33M Mar 15  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/libexec/gcc/x86_64-linux-gnu/14/cc1
    -rwxr-xr-x. 1 root root 35M Mar 15  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/libexec/gcc/x86_64-linux-gnu/14/cc1plus
    -rwxr-xr-x. 1 root root 32M Mar 15  2025 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/libexec/gcc/x86_64-linux-gnu/14/lto1
    -rwxr-xr-x. 1 root root 122M Oct 28 14:52 /var/lib/docker/  overlay2/ 4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e   07/merged/usr/local/lib/python3.13/site-packages/playwright/   driver/node
    -rwxr-xr-x. 1 root root 28M Oct 28 04:38 /var/lib/docker/   overlay2/  4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e    07/merged/usr/local/lib/libpython3.13.so.1.0
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/ 4fe7f06a187a38b40c6bcfe295f4aef876ed61eff38367d792a58d066c459e   07/merged/app/book_store_venv/lib/python3.13/site-packages/    playwright/driver/node
    -rwxr-xr-x. 1 root root 122M Oct 26 16:18 /var/lib/docker/  overlay2/on34ik6feg9646dixtuasyrj6/diff/app/book_store_venv/  lib/python3.13/site-packages/playwright/driver/node
    -rwxr-xr-x. 1 root root 26M Oct 19 18:54 /usr/bin/ctr
    -rwxr-xr-x. 1 root root 17M Sep 29 21:14 /usr/bin/  amazon-ssm-agent
    -rwxr-xr-x. 1 root root 27M Sep 29 21:14 /usr/bin/  ssm-agent-worker
    -rwxr-xr-x. 1 root root 22M Sep 29 21:14 /usr/bin/ssm-cli
    -rwxr-xr-x. 1 root root 25M Sep 29 21:14 /usr/bin/  ssm-document-worker
    -rwxr-xr-x. 1 root root 12M Sep 29 21:14 /usr/bin/  ssm-session-logger
    -rwxr-xr-x. 1 root root 21M Sep 29 21:14 /usr/bin/  ssm-session-worker
    -rwxr-xr-x. 1 root root 43M Oct 19 18:54 /usr/bin/containerd
    -rwxr-xr-x. 1 root root 17M Oct 19 18:54 /usr/bin/  containerd-shim-runc-v2
    -rwxr-xr-x. 1 root root 28M Oct 22 20:53 /usr/bin/docker
    -rwxr-xr-x. 1 root root 96M Oct 22 20:53 /usr/bin/dockerd
    -rwxr-xr-x. 1 root root 12M Oct 22 20:39 /usr/sbin/runc
    -rw-r--r--. 2 root root 214M Jul 13 12:13 /usr/lib/locale/  locale-archive
    -rw-r--r--. 2 root root 214M Jul 13 12:13 /usr/lib/locale/  locale-archive.real
    -rwxr-xr-x. 1 root root 14M Oct 19 19:42 /usr/lib/modules/6.    18.56-125.164.amzn2023.x86_64/vmlinuz
    -rw-r--r--. 1 root root 21M Oct 19 17:58 /usr/lib/python3.9/    site-packages/awscli/data/ac.index
    -r--r--r--. 1 root root 12M Oct 23 23:57 /usr/lib/udev/hwdb.    bin
    -rwxr-xr-x. 1 root root 64M Oct 22 20:53 /usr/libexec/docker/   cli-plugins/docker-buildx
    -rwxr-xr-x. 1 ec2-user ec2-user 122M Oct 26 16:18 /home/    ec2-user/book_store/book_store_venv/lib/python3.13/ site-packages/playwright/driver/node
    -rw-------. 1 ec2-user ec2-user 47M Oct 26 16:18 /home/ ec2-user/.cache/pip/http-v2/a/5/b/e/b/   a5bebc90dfcb70bad5d0b36ff9ea96c3bb05b9621e2b1e9526fc839f.body

</details>


After looking at the output, I realised I wasn't sure what to look for. After some research I decided to try pruning docker to free up space. 

docker prune: "Removes all unused containers, networks, images (both dangling and unused), unused build cache"

**Debug task**: Prune docker\
**Result**: 2.4GB saved
<details><summary>Docker prune results</summary>

    $ sudo systemctl stop docker
    $ docker system prune

    Deleted Containers:
    91c87d32bf277b9e19bd6ecc883154d9810da8966df5d774fef4f648a772f3  b6
    59b11f54ed560fdf8f13e2206508fb9a94dfbcb73e1a39807960b6bb7e1520  b0
    1f45bf3b4ef603622e1c5f03c98766f98859949217104e8847711840afadc1  38

    Deleted Images:
    deleted:    sha256:736c1bc1cb09ddff85c8430ee85a1f03224517490a3b1357f993fd3 f129c955b
    deleted:    sha256:7a5b978d6715d5eef9668ae28c38e92718185ccda9db70c71218804 dd10fd52c

    Deleted build cache objects:
    ijxajto4x9k4iql1bvinbuy0i
    vpbclq9jcp5y8yipqrq1fvy3i
    twc3ae4mb0nzz3utx1eq5w9q6
    dl7la10mtaq66hspat93egylm
    07qkpzzwggr6t8dcdz4donvdz
    5pjpmix3yyi5diry0hp60fjgx
    xvcx8u58usasrd90hhwzo07p0
    qj825ertfwpn4pcoqw7f579v2
    croqj9kfrob7g0dl9kbsilwvo
    m47umsayrecrrunujtt5op1io
    37bheh61dgflq8svfdwe1se39
    f21kn7tad5xjmrccs7var34sa
    rufehqsnpdcki6ejuf4nx65ph
    iuzqg3x6busltmy5c1zqntarr
    xfy8yy6hb1stwqlcy2cj27lit
    2fjhix15kdfuqm10ie4ye4tfk
    u2ui4iw7959fkuvw2air3kn9a
    9ht80aik1aml27doybn1vy9nh
    zh085k6wlgp1ag2qitptxbxjv
    b5fjti39jmglka4e5ta0n1xdz
    ohx9tr6ct5xprt6fbhhupvkbf
    5968jh1zz0apuw1zi2ok0iquy
    yfkj68p2mxs9dxdjhp56hkrva
    gsw2dbrxl837cj5b88aj8e4us
    onlkspykhze1zg3kmtrhpk9yl
    i09hj6enm13ayrumz0h1lnvxa
    jul0ea4g1fpeil4r64aheoi8s
    woudoqxmue5ixmqhb6kck97nw
    gf5zzi1eli8sddmm0xi9tt3gq
    qr5fkya8mel18c2t2y3jsoosh

    Total reclaimed space: 2.4GB
</details>

Now with so much space saved are we finally able to deploy successfully? Well...

**Step**: Ensure database is running\
**Result**: No such container: book_store_db
<details><summary>Docker run db output</summary>

    ======CMD======
    if [ ! "$(docker ps -aq -f name=book_store_db)" ]; then
      docker run \
        --name book_store_db \
        --network book_store_network \
        -e POSTGRES_USER='***' \
        -e POSTGRES_PASSWORD='***' \
        -e POSTGRES_DB='book_store' \
        -d ***:17
      docker exec -i book_store_db psql -U *** -d book_store < ~/   book_store/seeds/books.sql
      docker exec -i book_store_db psql -U *** -d book_store < ~/   book_store/seeds/users.sql
    fi

    ======END======
    err: Unable to find image '***:17' locally
    err: 17: Pulling from library/***
    err: 6fc242d221a6: Pulling fs layer
    err: e6095e4c4fdd: Pulling fs layer
    err: bad9dce990ef: Pulling fs layer
    err: 904defe665c0: Pulling fs layer
    err: 455e5ed72fb1: Pulling fs layer
    err: 55f036305357: Pulling fs layer
    err: db07174d12aa: Pulling fs layer
    err: 03f2ecc50d4c: Pulling fs layer
    err: ff7cbe54dfda: Pulling fs layer
    err: 0a26f79bdef8: Pulling fs layer
    err: 1f1fbc5e4aa5: Pulling fs layer
    err: 7f824adc2669: Pulling fs layer
    err: 3cecd013db3b: Pulling fs layer
    err: 7f0980702fb2: Pulling fs layer
    err: docker: open /var/lib/docker/tmp/GetImageBlob1767105094:   no such file or directory.
    err: See 'docker run --help'.
    err: Error response from daemon: No such container:     book_store_db
    err: Error response from daemon: No such container:     book_store_db
    2026/10/30 17:23:22 Process exited with status 1

</details>


It seems the book_store_db container can't be created as docker is having issues pulling the postgres image for whatever reason.

I also replicated this error when running the db docker run command via SSH.

Armed with this information and the hubris of an expert engineer, I decided to carry out the obvious debugging step. Turn docker off and on again.

    $ sudo systemctl restart docker

A quick docker ps to be safe showed no db containers running.

Now with the problem definitely fixed, lets see what happened.

**Debug task**: Docker run db container\
**Result**: network book_store_network not found
<details><summary>Docker run db output</summary>

    $ docker run   --name book_store_db   --network     book_store_network   -e POSTGRES_USER=postgres   -e     POSTGRES_PASSWORD=password   -e POSTGRES_DB=book_store   -d     postgres:17
    Unable to find image 'postgres:17' locally
    17: Pulling from library/postgres
    6fc242d221a6: Pull complete
    e6095e4c4fdd: Pull complete
    bad9dce990ef: Pull complete
    904defe665c0: Pull complete
    455e5ed72fb1: Pull complete
    55f036305357: Pull complete
    db07174d12aa: Pull complete
    03f2ecc50d4c: Pull complete
    ff7cbe54dfda: Pull complete
    0a26f79bdef8: Pull complete
    1f1fbc5e4aa5: Pull complete
    7f824adc2669: Pull complete
    3cecd013db3b: Pull complete
    7f0980702fb2: Pull complete
    Digest:     sha256:31ba9c94a03ada9988f2bb493a22a75eef3a185884533e5cdbcd498  ea835b08f
    Status: Downloaded newer image for postgres:17
    126d8ef2abcf8b57e92ac20420b2d845edadbe4aff6d0c586769fcb6239b92  0d
    docker: Error response from daemon: network     book_store_network not found.

</details>

Oh, it actually worked. Time to recreate the network which was deleted after pruning.

    $ docker network create book_store_network


    $ docker network ls
    NETWORK ID     NAME                 DRIVER    SCOPE
    aa1305514b81   book_store_network   bridge    local
    416674b591e3   bridge               bridge    local
    90471e2c855e   host                 host      local
    01ecba616ac0   none                 null      local

Now with the network recreated and deployment now successful, we're home free right?

Not quite, the deploy script checks that book_store_db exists and if not runs docker run to create it. But in my case, it did exist, but was not running, resulting in navigating to /books complain about no books table existing.
This could have been spotted via the shell with the following:

    $docker ps -a

The -a flag shows stopped containers as well.

This will also show if you try to create the container again in response to the table not being found:

    $ docker run   --name book_store_db   --network     book_store_network   -e POSTGRES_USER=postgres   -e     POSTGRES_PASSWORD=password   -e POSTGRES_DB=book_store   -d     postgres:17
    docker: Error response from daemon: Conflict. The container     name "/book_store_db" is already in use by container     "126d8ef2abcf8b57e92ac20420b2d845edadbe4aff6d0c586769fcb6239b9    20d". You have to remove (or rename) that container to be     able to reuse that name.

This is solved by starting the stopped container:

    $docker start book_store_db

And to double check, list running containers again:

    $ docker ps
    CONTAINER ID   IMAGE               COMMAND                      CREATED              STATUS                  PORTS                                       NAMES
    be9048ee0912   book_store:latest   "python app.py"              About a minute ago   Up About a minute   0.0.0.0:5001->5001/    tcp, :::5001->5001/tcp   book_store
    126d8ef2abcf   postgres:17         "docker-entrypoint.s…"   3     minutes ago        Up 2 seconds        5432/    tcp                                    book_store_db

Now, to be safe I reseeded the tables and we were good to go!

    $ docker exec -i book_store_db     psql -U postgres -d book_store < ~/book_store/seeds/books.sql
    CREATE TABLE
    TRUNCATE TABLE
    INSERT 0 1
    INSERT 0 1
    INSERT 0 1
    INSERT 0 1
    $ docker exec -i book_store_db     psql -U postgres -d book_store < ~/book_store/seeds/users.sql
    CREATE TABLE
    TRUNCATE TABLE