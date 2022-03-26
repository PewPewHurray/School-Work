import {useState, useEffect} from "react";

const PokemonAPI = (props) => {
    const [pokemon, setPokemon] = useState([]);

    useEffect(() => {
        fetch("https://pokeapi.co/api/v2/pokemon?limit=807")
        .then(response => response.json())
        .then(response => setPokemon(response.results))
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