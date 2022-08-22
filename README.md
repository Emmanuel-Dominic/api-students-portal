# API-students-portal
A student portal project that acts as an online portal between students and the admin built using GraphQL with Django.

## Project Setup

- ### Setup virtual-environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- ### Run Project
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- ### Run Tests
 - [x] unittests & snapshots
    - ```coverage run --source='.' manage.py test```
    ![Screenshot from 2022-08-22 19-59-39](https://user-images.githubusercontent.com/50827537/185996421-f0fd563c-d969-4a86-8fe5-383048cf3fc3.png)

 - [x] pytest
    - ```pytest```
    ![Screenshot from 2022-08-22 21-46-31](https://user-images.githubusercontent.com/50827537/185996445-5241ef29-39d8-4943-bcb9-80138f459e78.png)

### GraphQL Query

- #### Get all users
```
query {
    users {
        id
        email
        username
        isActive
        isSuperuser
        dateJoined
    }
}
```

- #### Get a single user
```
query user($pk: Int!) {
    user(pk: $pk) {
        id
        email
        username
        isActive
        isSuperuser
        dateJoined
    }
}

variables = {"courseId": 1}
```

- #### Get all courses
```
query {
    courses {
        id
        name
        description
    }
}
```

- #### Get a single course
```
query course($courseId: ID!) {
    course(courseId: $courseId) {
        id
        name
        description
    }
}

variables = {"courseId": 1}
```

- #### Get all students
```
query {
    students {
        id
        email
        username
        isActive
        course {
            id
            name
            description
        }
    }
}
```

- #### Get a single student
```
query student($studentId: ID!) {
    student(studentId:$studentId) {
        id
        email
        username
        isActive
        course {
            id
            name
            description
        }
    }
}

variables = {"studentId": 1}
```

### GraphQL Mutation

- #### Create new course
```
mutation createCourse($name: String!, $description: String!) {
    createCourse(name: $name, description: $description) {
        course {
            id 
            name
            description
        }
    }
}

variables = {name:"course name", description:"course description"}
```

- #### Create new student
```
mutation createStudent($username: String!, $email: String!, $firstName: String!, $lastName: String!, $gender: String!, 
$password: String!, courseId: Int!, isActive: String!) {
    createStudent(username: $username, email: $email, firstName: $firstName, lastName: $lastName, gender: $gender, 
    password: $password, courseId: $courseId, isActive: $isActive) {
        student {
             id 
             username
             email
             firstName
             lastName
             gender
             password
             isActive
             course { 
                id 
                name 
                description
             }
        }
    }
}

variables = {
    username:"tomas", email:"tomas@gmail.com", firstName:"dollar", lastName:"tomas", gender:"female", 
    password:"tomas123", courseId:1, isActive: "t"}
```

- #### Update course by id
```
mutation updateCourse($pk: ID!, $name: String, $description: String) {
    updateCourse(pk: $pk, name: $name, description: $description) {
        course {
            id 
            name
            description
        }
    }
}

variables = {pk:2, name: "updated name", description: "updated description"}
```

- #### Update student by id
```
mutation updateStudent($pk: ID!, $username: String, $email: String, $firstName: String, $lastName: String, 
$gender: String, $password: String, courseId: Int, isActive: String) {
    updateStudent(pk: $pk, username: $username, email: $email, firstName: $firstName, lastName: $lastName, gender: $gender, 
    password: $password, courseId: $courseId, isActive: $isActive) {
        student {
             id 
             username
             email
             firstName
             lastName
             gender
             password
             isActive
             course { 
                id 
                name 
                description
             }
        }
    }
}

variables = {
    pk:1, username:"manuel", email:"manuel@gmail.com", firstName:"dollar", lastName:"dominic", gender:"male", 
    password:"Password123", courseId:1, isActive: "t"}
```

- #### Delete course by id
```
mutation deleteCourse($pk: ID!) {
    deleteCourse(pk: $pk) {
        message 
    }
}

variables = {"pk": 1}
```

- #### Delete student by id
```
mutation ($pk: ID!) {
    deleteStudent(pk: $pk) {
        message 
    }
}

variables = {"pk": 1}
```
