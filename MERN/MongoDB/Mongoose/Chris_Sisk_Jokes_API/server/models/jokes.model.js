const mongoose = require("mongoose");

const JokeSchema = new mongoose.Schema({
    setup: {
        type: String,
        required: "Setup can not be blank"
    },
    punchLine: {
        type: String,
        required: "Punch line can not be blank"
    }},
    { timestamps: true}
);

const Joke = mongoose.model("Joke", JokeSchema);

module.exports = Joke;