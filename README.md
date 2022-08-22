# API-students-portal
A student portal project that acts as an online portal between students and the admin built using GraphQL with Django.


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
