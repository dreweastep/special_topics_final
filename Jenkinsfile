pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        //build - just in case, make sure modules are there
        echo 'Just make sure the necessary python stuff is there'
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        //run a simple test, does /index return 200 OK
        sh 'python3 test.py'
      }   
    }
    stage('deploy') {
      steps {
        //zip up the files.  Move to a deploy folder
         echo 'zipping files'
         sh 'pwd'
         sh 'ls -las'
         sh 'tar -czvf flaskapi.tar.gz *'
         sh 'mv flaskapi.tar.gz /home/deploy'
      } 
    }
  }
}
