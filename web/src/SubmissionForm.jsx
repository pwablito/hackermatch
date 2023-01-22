import React from "react";
import LabelledSpinner from "./LabelledSpinner";
import {submitHash} from "./Net";

class SubmissionForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      hash: "",
      loading: false,
      error: false,
      success: false,
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleUploadButtonClick = this.handleUploadButtonClick.bind(this);
    this.submitRequest = this.submitRequest.bind(this);

    this.uploadButtonRef = React.createRef();
  }

  async submitRequest(e) {
    e.preventDefault();
    try {
      this.trigger_error_banner();
      await submitHash(
        this.state.hash,
        this.state.email,
      );
      this.trigger_success_banner();
    } catch (e) {
      this.trigger_error_banner();
    }
  }

  trigger_loading() {
    this.setState(
      {
        loading: true,
        error: false,
        success: false,
      },
      (_) => {
        this.render();
      }
    );
  }

  trigger_error_banner() {
    this.setState(
      {
        loading: false,
        error: true,
        success: false,
      },
      (_) => {
        this.render();
        this.clear_banners_after_delay();
      }
    );
  }
  trigger_missing_fields_banner() {
    this.setState(
      {
        loading: false,
        error: false,
        success: false,
      },
      (_) => {
        this.render();
        this.clear_banners_after_delay();
      }
    );
  }

  trigger_success_banner() {
    this.setState(
      {
        loading: false,
        success: true,
        error: false,
      },
      (_) => {
        this.render();
        this.clear_banners_after_delay();
      }
    );
  }

  clear_banners_after_delay() {
    setTimeout((_) => {
      this.setState({
        loading: false,
        error: false,
        success: false,
      });
      this.render();
    }, 5000); // 5 second delay
  }

  handleChange(e) {
    const changed_field = e.target.name;
    const new_value = e.target.value;

    this.setState({
      [changed_field]: new_value,
    });
  }

  handleFileChange(e) {
    this.setState({
      file: e.target.files[0],
    });
  }

  handleUploadButtonClick(_) {
    this.uploadButtonRef.current.click();
  }

  render() {
    return (
      <div>
        <div>
          <form onSubmit={this.submitRequest}>
            <div className="form-group">
              <label htmlFor="name">Hash</label>
              <input
                type="text"
                className="form-control"
                id="hash"
                name="hash"
                placeholder="Enter your hash"
                value={this.state.hash}
                onChange={this.handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                className="form-control"
                id="email"
                name="email"
                placeholder="Enter your email"
                value={this.state.email}
                onChange={this.handleChange}
              />
            </div>
            <button
              type="submit"
              className="btn btn-primary"
              onClick={this.submitRequest}
            >
              Submit
            </button>
          </form>
        </div>
        {this.state.loading && <LabelledSpinner label="Submitting" />}
        {this.state.error && (
          <p style={{ color: "red" }}>Something went wrong</p>
        )}
        {this.state.success && <p style={{ color: "green" }}>Submitted</p>}
      </div>
    );
  }
}

export default SubmissionForm;
