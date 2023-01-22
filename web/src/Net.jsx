import axios from "axios";

const submitHash = async (hash, email) => {
  let res = await axios.post("/api/submission/submit", {
    hash: hash,
    email: email,
  });
  console.log(res)
  if (!res.data.success)
    // eslint-disable-next-line no-throw-literal
    throw {
      error: res.data.message,
    };
};

export { submitHash };
