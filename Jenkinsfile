pipeline {
    environment { 
        registry = "sonikxsvg/ci_cd" 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
              }
    agent any
    stages {
        stage('Build') {
            steps {
                //sh 'sudo usermod -aG docker jenkins'
                sh 'echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
                // Get some code from a GitHub repository
                git url: 'https://github.com/SonicX-svg/MLOps_itogProject_.git', branch: 'first_experiment'
         stages {
            steps { 
                script { dockerImage = docker.build registry + ":$BUILD_NUMBER"}}}
         stages {
            steps { 
                script { docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() }}}
         stages {
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" }}
             
                sh 'dockerImage = docker.build registry'
                // Change file permisson
                sh "chmod +xrw -R /var/lib/jenkins/workspace/MLOps2"
                // Run shell script - привет
                sh 'pwd'
                sh "./hello_there.sh"
                
                
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
