pipeline {
    agent {
        node {
            label 'new-py-template'
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
            pip3 install click
            python3 helloworld.py
            '''
            }
        }
    }
}