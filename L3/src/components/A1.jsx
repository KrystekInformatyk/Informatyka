import React, { useState } from "react";
import a1 from "./img/a1.jpg";
import a2 from "./img/a2.jpg";
import a3 from "./img/a3.jpg";

function A1() {
  const [state, setState] = useState(0);

  const increaseState = () => {
    setState(state + 1);
  };

  const reset = () => {
    setState(0);
  };

  const decreaseState = () => {
    setState(state - 1);
  };

  const imgDisplay = () => {
    if (state < 10) {
      return <img src={a1} alt="" />;
    } else if (state >= 10 && state < 20) {
      return <img src={a2} alt="" />;
    } else {
      return <img src={a3} alt="" />;
    }
  };

  return (
    <div>
      <p>State: {state}</p>
      <button onClick={increaseState}>Increase State</button>
      <button onClick={decreaseState}>Decrease State</button>
      <button onClick={reset} RESET></button>
      <div>{imgDisplay()}</div>
    </div>
  );
}

export default A1;
