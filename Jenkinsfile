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
                    git url: 'https://github.com/SonicX-svg/MLOps_itogProject_.git', branch: 'first_experiment'}}
        stage {
                steps { 
                    script { dockerImage = docker.build registry + ":$BUILD_NUMBER"}}}
        stage {
                steps { 
                    script { docker.withRegistry( '', registryCredential ) { 
                            dockerImage.push() }}}}
        stage('Create_model') {
                steps {
                      sh 'python eda.py'
                      sh 'python model_creation.py'
                      sh 'python test_model.py'}
            
          }
    }
          //stage('Tests') {
     // }
    }

