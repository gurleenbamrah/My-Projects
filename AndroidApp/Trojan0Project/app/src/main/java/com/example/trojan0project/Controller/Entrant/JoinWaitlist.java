package com.example.trojan0project.Controller.Entrant;

import android.location.Address;
import android.location.Geocoder;
import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.trojan0project.View.Entrant.JoinWaitlistFragment;
import com.example.trojan0project.Model.Profile;
import com.example.trojan0project.R;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.SetOptions;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * Purpose:
 * This retrieves events and user profile information from firestore and displays it.
 * Users view event details and join the events waitlist by pressing confirm.
 *
 * Design Rationale:
 * Uses Firebase Firestore to get event and user data and poster. Uses JoinWaitlistFragment dialog to confirm
 * if the user wants to join the waitlist.
 *
 * Outstanding issues:
 * If user wants to sign someone other than them, the code does not do that.
 *
 */

public class JoinWaitlist extends AppCompatActivity implements JoinWaitlistFragment.JoinWaitlistListener {

    private static final String TAG = "JoinWaitlist";
    private FirebaseFirestore db;
    private String deviceId;
    private String eventId;
    private String eventName;
    private Double latitude;
    private Double longitude;
    private Double userLatitude;
    private Double userLongitude;
    private String time;
    private String description;

    private TextView eventTitle;
    private TextView eventLocation;
    private TextView eventTime;
    private TextView eventMoreInfo;
    private Button joinWaitlistButton;

    /**
     * Initializes the activity and loads the event details.
     *
     * @param savedInstanceState The saved state of the activity.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_join_waitlist);

        Log.d(TAG, "onCreate: Activity started");

        db = FirebaseFirestore.getInstance();

        deviceId = Settings.Secure.getString(getContentResolver(), Settings.Secure.ANDROID_ID);
        Log.d(TAG, "onCreate: Device ID = " + deviceId);
        eventId = getIntent().getStringExtra("eventId");
        eventName = getIntent().getStringExtra("eventName");
        latitude = getIntent().getDoubleExtra("latitude", 0.0);
        longitude = getIntent().getDoubleExtra("longitude", 0.0);
        userLatitude = getIntent().getDoubleExtra("currentLatitude", 0.0);
        userLongitude = getIntent().getDoubleExtra("currentLongitude", 0.0);
        time = getIntent().getStringExtra("time");
        description = getIntent().getStringExtra("description");

        Log.d(TAG, "onCreate: Event Details - eventId: " + eventId + ", eventName: " + eventName +
                ", latitude: " + latitude + ", longitude: " + longitude + ", time: " + time + ", description: " + description);

        // Reference views
        eventTitle = findViewById(R.id.event_title);
        eventLocation = findViewById(R.id.location_label);
        eventTime = findViewById(R.id.time_label);
        eventMoreInfo = findViewById(R.id.more_info_label);
        joinWaitlistButton = findViewById(R.id.join_waitlist_button);

        loadEventDetails();
        getEventPoster();

        joinWaitlistButton.setOnClickListener(v -> {
            Log.d(TAG, "onCreate: Join Waitlist button clicked");
            getUserProfileForDialog();
        });
    }

    /**
     * Converts latitude and longitude coordinates to a human-readable address.
     *
     * @param latitude  The latitude of the location.
     * @param longitude The longitude of the location.
     * @return A string address based on the coordinates or an error message if unavailable.
     */
    //From https://www.geeksforgeeks.org/reverse-geocoding-in-android/ , 2024-11-07
    public String getAddressFromCoordinates(double latitude, double longitude) {
        Log.d(TAG, "getAddressFromCoordinates: Converting coordinates to address: latitude = " + latitude + ", longitude = " + longitude);
        Geocoder geocoder = new Geocoder(this, Locale.getDefault());
        try {
            List<Address> addresses = geocoder.getFromLocation(latitude, longitude, 1);
            if (addresses != null && !addresses.isEmpty()) {
                Address address = addresses.get(0);
                Log.d(TAG, "getAddressFromCoordinates: Address found = " + address.getAddressLine(0));
                return address.getAddressLine(0);
            } else {
                Log.w(TAG, "getAddressFromCoordinates: Address not found");
                return "Address not found";
            }
        } catch (IOException e) {
            Log.e(TAG, "getAddressFromCoordinates: Geocoder service not available", e);
            return "Geocoder service not available";
        }
    }
    /**
     * Loads the event details from Firestore and displays them in the UI.
     */
    private void loadEventDetails() {
        Log.d(TAG, "loadEventDetails: Fetching event details for eventId = " + eventId);
        db.collection("events").document(eventId).get()
                .addOnSuccessListener(documentSnapshot -> {
                    if (documentSnapshot.exists()) {
                        Log.d(TAG, "loadEventDetails: Event document found");
                        String title = documentSnapshot.getString("eventName");
                        Double latitude = documentSnapshot.getDouble("latitude");
                        Double longitude = documentSnapshot.getDouble("longitude");
                        String time = documentSnapshot.getString("time");
                        String description = documentSnapshot.getString("description");

                        if (latitude != null && longitude != null){
                            String address = getAddressFromCoordinates(latitude, longitude);
                            eventLocation.setText(address);
                        } else {
                            Log.w(TAG, "loadEventDetails: Latitude or longitude is null");
                        }

                        eventTitle.setText(title != null ? title : "No Title");
                        eventTime.setText(time != null ? time : "No Time");
                        eventMoreInfo.setText(description != null ? description : "No Description");
                    } else {
                        Toast.makeText(this, "Event not found", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "loadEventDetails: Failed to load event details", e);
                    Toast.makeText(this, "Failed to load event details: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });
    }

    /**
     * Gets and displays the poster for a specific event
     * Retrieves posterPath from Firestore for the event id
     * If poster is found then uses Glide to load the image into the ImageView
     */
    public void getEventPoster() {
        Log.d(TAG, "getEventPoster: Fetching poster for eventId = " + eventId);
        db.collection("events").document(eventId)
                .get()
                .addOnSuccessListener(documentSnapshot -> {
                    if (documentSnapshot.exists()) {
                        String posterPath = documentSnapshot.getString("posterPath");
                        if (posterPath != null) {
                            Log.d(TAG, "getEventPoster: Poster path found = " + posterPath);
                            ImageView eventPoster = findViewById(R.id.event_poster);
                            Glide.with(this)
                                    .load(posterPath)
                                    .into(eventPoster);
                            Log.d("EventPoster", "Poster loaded: " + posterPath);
                        } else {
                            Log.w(TAG, "getEventPoster: No poster available");
                            Toast.makeText(this, "No poster available for this event", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        Toast.makeText(this, "Event not found", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "getEventPoster: Error loading poster", e);
                    Toast.makeText(this, "Error loading poster: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });
    }


    /**
     * Retrieves the user's profile data to populate the dialog when joining the waitlist.
     */
    private void getUserProfileForDialog(){
        db.collection("users").document(deviceId).get()
                .addOnSuccessListener(documentSnapshot -> {
                    if (documentSnapshot.exists()) {
                        String firstName = documentSnapshot.getString("first_name");
                        String lastName = documentSnapshot.getString("last_name");
                        String email = documentSnapshot.getString("email");

                        Log.d(TAG, "getUserProfileForDialog: User profile found: firstName = " + firstName +
                                ", lastName = " + lastName + ", email = " + email);

                        Profile profile = new Profile(firstName, lastName, email);

                        // Open waitlist dialog with user profile
                        JoinWaitlistFragment dialog = new JoinWaitlistFragment(profile);
                        dialog.show(getSupportFragmentManager(), "JoinWaitlistFragment");
                    } else {
                        Toast.makeText(this, "User profile not found", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "getUserProfileForDialog: Error fetching user profile", e);
                    Toast.makeText(this, "Error getting user profile: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });
    }

    /**
     * Confirms the user's intent to join the waitlist and updates Firestore with the waitlist entry.
     *
     * @param profile The user's profile data used to join the waitlist.
     */
    @Override
    public void onConfirm(Profile profile) {
        if (deviceId == null) {
            Log.e(TAG, "Device ID is null. Cannot proceed with waitlist addition.");
            Toast.makeText(this, "Device ID is not available. Please try again.", Toast.LENGTH_SHORT).show();
            return;
        }

        Log.d(TAG, "Starting waitlist confirmation for Device ID: " + deviceId + " and Event ID: " + eventId);

        // Fetch event details to check max entrants and current waitlist size
        db.collection("events").document(eventId).get()
                .addOnSuccessListener(eventSnapshot -> {
                    if (eventSnapshot.exists()) {
                        Log.d(TAG, "Event document found for Event ID: " + eventId);

                        // Retrieve maxNumberOfEntrants
                        int maxEntrants = eventSnapshot.contains("maxNumberOfEntrants") ?
                                eventSnapshot.getLong("maxNumberOfEntrants").intValue() : Integer.MAX_VALUE;

                        // Retrieve current waitlist size
                        Map<String, Object> users = (Map<String, Object>) eventSnapshot.get("users");
                        int currentWaitlistSize = (users != null) ? users.size() : 0;

                        Log.d(TAG, "Max Entrants: " + maxEntrants + ", Current Waitlist Size: " + currentWaitlistSize);

                        // Check if the waitlist is full
                        if (currentWaitlistSize >= maxEntrants) {
                            Toast.makeText(this, "Waitlist is full!", Toast.LENGTH_SHORT).show();
                            return; // Stop further execution
                        }

                        // Proceed to add the user to the waitlist
                        addToWaitlist(profile);
                    } else {
                        Log.w(TAG, "Event not found for Event ID: " + eventId);
                        Toast.makeText(this, "Event not found. Please try again later.", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "Failed to retrieve event details for Event ID: " + eventId, e);
                    Toast.makeText(this, "Failed to load event details. Please try again.", Toast.LENGTH_SHORT).show();
                });
    }

    private void addToWaitlist(Profile profile) {
        Log.d(TAG, "Adding user to waitlist with Device ID: " + deviceId + " and Event ID: " + eventId);

        // Update 'events' field
        Map<String, Object> eventsData = new HashMap<>();
        eventsData.put(eventId, 0);

        // Update 'geolocation' field
        Map<String, Object> geolocationData = new HashMap<>();
        geolocationData.put(eventId, Arrays.asList(userLatitude, userLongitude)); // Longitude at index 0, Latitude at index 1

        // Prepare the updates for the user's document
        Map<String, Object> userUpdates = new HashMap<>();
        userUpdates.put("events", eventsData);
        userUpdates.put("geolocation", geolocationData);

        // Update the user's document in Firestore
        db.collection("users").document(deviceId)
                .set(userUpdates, SetOptions.merge()) // Merge updates without overwriting unrelated fields
                .addOnSuccessListener(aVoid -> {
                    Log.d(TAG, "Successfully updated user's document with events and geolocation.");
                    Toast.makeText(this, "You have been waitlisted for the event.", Toast.LENGTH_SHORT).show();
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "Failed to update user's document: " + e.getMessage());
                    Toast.makeText(this, "Failed to update your waitlist status: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });

        // Update the 'users' field for the event
        Map<String, Object> userMap = new HashMap<>();
        userMap.put(deviceId, 0);

        db.collection("events").document(eventId)
                .set(Collections.singletonMap("users", userMap), SetOptions.merge())
                .addOnSuccessListener(aVoid -> {
                    Log.d(TAG, "Successfully added user to the event's waitlist.");
                })
                .addOnFailureListener(e -> {
                    Log.e(TAG, "Failed to add user to event's waitlist: " + e.getMessage());
                    Toast.makeText(this, "Failed to update event waitlist: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });
    }
}