pipeline {
    agent {
        node {
            label 'venv-agent'
        }
    }
    stages {
        stage('who') {
            steps{
            sh '''
            whoami
            ls -la
            echo "the BUILD ID is ${BUILD_ID}"
            '''
            }
        }
        stage('pre-run') {
            steps{
            sh '''
            python3 helloworld.py
            echo "installing requirements"
            python3 --version
            pip3 --version
            '''
            }
        }
        stage('build') {
            steps{
            sh '''
            cd sensor-processor/
            pip install --break-system-packages -r requirements.txt
            python3 start.py --ping
            '''
            }
        }
        stage('test') {
            steps {
                sh'''
                python3 -m unittest tests.test_mock_script
                '''
            }       
        }
    }
}