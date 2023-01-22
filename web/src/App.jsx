import "./App.css";
import React from "react";
import SubmissionForm from "./SubmissionForm";

const App = React.forwardRef((_, __) => {
  return (
    <div className="App">
      <h1>Welcome to the HackerMatch web client</h1>
      <p>Please enter your hash and a contact email here.</p>
      <p>We will send you an email if/when someone else submits the same hash as you.</p>
      <p>If someone has already submitted your hash, you should expect an email from us soon!</p>
      <SubmissionForm/>
    </div>
  );
});

export default App;
