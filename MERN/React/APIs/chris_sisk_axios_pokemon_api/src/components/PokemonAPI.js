import {useState, useEffect} from "react";
import axios from "axios";

const PokemonAPI = (props) => {
    const [pokemon, setPokemon] = useState([]);

    useEffect(() => {
        axios.get("https://pokeapi.co/api/v2/pokemon?limit=807")
            .then(response => setPokemon(response.data.results))
            .catch(console.log("No Data"))
    }, []);

    return(
        <div>
            <h1>Pokemon</h1>
            <ul>
                {pokemon.length > 0 && pokemon.map((onePokemon, index) => {
                    return (<li key={index}>{onePokemon.name}</li>)
                })}
            </ul>
        </div>
    );
}

export default PokemonAPI;