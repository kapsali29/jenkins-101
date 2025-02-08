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
        stage('run') {
            steps{
            sh '''
            python3 helloworld.py
            '''
            }
        }
    }
}