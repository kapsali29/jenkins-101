pipeline {
    agent { 
        node {
            label 'pka-python-agent'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                echo "the build is ${BUILD_ID}"
                '''
            }
        }
    }
}