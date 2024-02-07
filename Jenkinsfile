pipeline {
    agent any

    environment {
        PYTHONPATH = "/var/lib/jenkins/workspace/streamcropper_pipeline/streamcropper:/var/lib/jenkins/workspace/streamcropper_pipeline/test"
    }

    stages {
        stage('Pip install packages') {
            steps {
               sh "pip3 install -r requirements.txt"
            }
        }

        stage('Move config file') {
            steps {
               sh "cp /var/lib/jenkins/streamcropper_configs/twith_platform.py streamcropper/twith_platform/config.py"
            }
        }

        stage('Fast test') {
            steps {
                dir('test') {
                    sh "nosetests -v streamcopper"
                }
            }
        }

        stage('Slow test') {
            steps {
                dir('test') {
                    sh "nosetests --nocapture -v slow"
                }
            }
        }

        stage("Restart prev watchers") {
            steps {
                sh "sudo /usr/bin/systemctl restart streamcropper-watcher"
            }
        }

        stage('Restart web') {
             steps {
                 sh "sudo /usr/bin/systemctl restart streamcropper-web"
             }
        }

        stage('Deploy react') {
            steps {
                sh "npm install --prefix streamcropper/gui/react-app"
                sh "npm run build --prefix streamcropper/gui/react-app"
                sh "cp -r streamcropper/gui/react-app/build/* /webserver"
            }
        }
    }
}