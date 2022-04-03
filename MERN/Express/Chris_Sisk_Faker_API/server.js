const express = require("express");
const app = express();
const port = 8000;
const faker = require("faker");

const createUser = (props) => {
    const firstName = faker.name.firstName();
    const lastName = faker.name.lastName();
    const newUser = {
        _id: faker.datatype.number(),
        firstName: firstName,
        lastName: lastName,
        phoneNumber: faker.phone.phoneNumber("###-###-####"),
        email: faker.internet.email(firstName, lastName),
        password: faker.internet.password()
    }
    return newUser;
}

const createCompany = () => {
    const state = faker.address.stateAbbr();
    const newCompany = {
        _id: faker.datatype.number(),
        name: faker.company.companyName(),
        address: {
            street: faker.address.streetAddress(),
            city: faker.address.cityName(),
            state: state,
            zipCode: faker.address.zipCode(),
            county: faker.address.county()
        }
    }
    return newCompany;
}

app.get("/api/users/new", (req, res) => {
    res.json(createUser());
});

app.get("/api/companies/new", (req, res) => {
    res.json(createCompany());
});

app.get("/api/user/company", (req, res) => {
    res.json([createUser(), createCompany()]);
});

app.listen( port, () => console.log(`Listening on port: ${port}`));