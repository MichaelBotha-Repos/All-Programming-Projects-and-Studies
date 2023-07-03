type Person={
    firstName: string
    lastName: string
    title: string
    age: number
}

type Task = {
    description: string
    assignedTo: Person
    startDate: Date
    endDate: Date
}