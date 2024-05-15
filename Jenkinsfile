pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git url: 'https://github.com/naiveskill/devops.git', branch: 'main'
                // Change file permisson
                sh "chmod +xrw -R /var/lib/jenkins/workspace/eee"
                // Run shell script - привет
                sh "/var/lib/jenkins/workspace/eee/hello_there.sh"
                sh 'docker build Dockerfile .'
            }
           steps {
                sh """
                  docker build Dockerfile .
                """
                }
          steps {
                sh """
                  docker run --rm Dockerfile
                """
      }
    }
      stage('Create_model') {
                  steps {
                     sh 'python eda.py'}
                    steps { sh 'python model_creation.py'}
                  steps {   sh 'python test_model.py'}
        
      }
      stage('Tests') {
  }
}
