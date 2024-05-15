pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git url: 'https://github.com/SonicX-svg/MLOps_itogProject_.git', branch: 'first_experiment'
                // Change file permisson
                sh "chmod +xrw -R /var/lib/jenkins/workspace/eee"
                // Run shell script - привет
                sh "/var/lib/jenkins/workspace/eee/hello_there.sh"
                sh 'pwd'
                
                sh """
                  docker build -k dockerfile .
                """

                sh """
                  docker run --rm dockerfile
                """
      }
    }
      stage('Create_model') {
                  steps {
                     sh 'python eda.py'
                    sh 'python model_creation.py'
                   sh 'python test_model.py'}
        
      }
      //stage('Tests') {
 // }
}
}
