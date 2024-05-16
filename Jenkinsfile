pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //sh 'sudo usermod -aG docker jenkins'
                sh 'echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
                // Get some code from a GitHub repository
                git url: 'https://github.com/SonicX-svg/MLOps_itogProject_.git', branch: 'first_experiment'
                // Change file permisson
              //  sh "chmod +xrw -R /var/lib/jenkins/workspace/MLOps2"
                // Run shell script - привет
                sh "hello_there.sh"
                
                
                sh """
                  docker build  dockerfile 
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
