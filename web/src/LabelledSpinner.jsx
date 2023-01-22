import { Spinner } from "react-bootstrap";

function LabelledSpinner(props) {
    return (
        <div>
            <p>{props.label}</p>
            <Spinner animation="grow" variant="primary" />
        </div>
    )
}

export default LabelledSpinner;