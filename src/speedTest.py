#pip install speedtest-cli

import speedtest

def test_speedtest_cli():
    print("Testing with speedtest-cli...")
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download()
    print(f"Download speed: {download_speed / 1_000_000:.2f} Mbps") # Convert to Mbps

    upload_speed = st.upload()
    print(f"Upload speed: {upload_speed / 1_000_000:.2f} Mbps") # Convert to Mbps
    
    ping = st.results.ping
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    test_speedtest_cli()
