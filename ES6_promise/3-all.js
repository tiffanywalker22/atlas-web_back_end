import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto, createUser])
    .then((response) => {
      console.log(`${response.body} ${response.firstname} ${response.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
