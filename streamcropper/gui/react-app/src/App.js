import './App.css';
import IndexPage from "./page/IndexPage";
import {useEffect} from "react";

function App() {
    useEffect(() => {
        document.title = global.title;
    });

  return (
    <div className="App">
        <IndexPage name="Sara" />
    </div>
  );
}

export default App;
