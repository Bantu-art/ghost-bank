import { Link, useForm } from "@inertiajs/react";

const Layout = ({children, ...props}) => {
  // Check if user is authenticated from Inertia shared props
  const isAuthenticated = props.isAuthenticated;
  const { post } = useForm({});

  const handleLogout = (e) => {
    e.preventDefault();
    post('/accounts/logout/', {
      onSuccess: () => window.location.href = '/' // fallback in case
    });
  };

  return (
    <>
    <nav className="border border-gray-400 mb-2 flex justify-center items-center">
      <ul className="flex gap-2">
        <li><Link href="/">Home</Link></li>
        <li><Link href="/contact">Contact</Link></li>
        {!isAuthenticated && <li><Link href="/accounts/login">Login</Link></li>}
        {!isAuthenticated && <li><Link href="/accounts/register">Register</Link></li>}
        {isAuthenticated && (
          <li>
            <form onSubmit={handleLogout} style={{display: 'inline'}}>
              <button type="submit" className="text-red-600 hover:underline bg-transparent border-none cursor-pointer">Logout</button>
            </form>
          </li>
        )}
      </ul>
    </nav>
    <main className="flex justify-center items-center">
      { children }
    </main>
    </>
  );
};

export default page => <Layout {...page.props}>{page}</Layout>;