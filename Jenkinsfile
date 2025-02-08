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
            '''
            }
        }
        stage('build') {
            steps{
            sh '''
            echo "installing requirements"
            pip install click
            '''
            }
        }
    }
}