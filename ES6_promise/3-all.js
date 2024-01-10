import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, createUser]) => {
      console.log(`${userResult.body} ${userResult.firstname} ${userResult.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
