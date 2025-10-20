import LoginForm from './components/LoginForm';

const Login = () => {
  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-100">
      <div className="w-full max-w-sm">
        <LoginForm />
      </div>
    </div>
  );
};

export default Login;